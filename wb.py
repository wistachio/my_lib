'''To surf the web, supply website to start
Possible start w = wb.web('www.google.com')
NOTE: If https, include as will only add http

Common Errors:
if can't find element, check in right frame
'''
import re
import selenium as s
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.common import exceptions as excp

import time
import sys

from bs4 import BeautifulSoup as bs


if sys.platform == 'linux':
    binary = FirefoxBinary(r'/usr/bin/firefox')
else:
    binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    
if sys.platform == 'linux':
    gecko_path = r'python/geckodriver'
else:
    gecko_path = r'Y:\python\geckodriver.exe'


    '''
xpath stuff

Xpath=//tagname[@attribute='value']

Absolute XPath:
/html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]

Relative XPath:
//div[@class='featured-box cloumnsize1']//h4[1]//b[1]

Egs
Xpath=//input[@type='text']				
Xpath=	//label[@id='message23']
Xpath=	//input[@value='RESET']
Xpath=//*[@class='barone']
Xpath=//a[@href='http://demo.guru99.com/']
Xpath= //img[@src='//cdn.guru99.com/images/home/java.png']

"//*[text()='I agree']"
//* :any tag
in above, any tag that has text 'I agree'

contains()
Xpath=//*[contains(@name,'btn')]
if value of btnLogin changed, can use partial text btn

and or
Xpath=//*[@type='submit' or @name='btnReset']

Xpath=//label[starts-with(@id,'message')]

Xpath=//td[text()='UserID']
the element contains the text visible to work 'UserID'

'''


##def contains_attr_value(elem,dic_attr_attr-values):
##    '''if supplied element contains given attribute and attribute value'''
##
##def __get_elems(driver,dic_args):
##    '''ID = "id_value"
##    XPATH = "xpath"
##    LINK_TEXT = "link text"
##    PARTIAL_LINK_TEXT = "partial link text"
##    NAME = "name"
##    TAG_NAME = "tag name"
##    CLASS_NAME = "class name"
##    CSS_SELECTOR = "css selector"
##    '''
##    #get list of elems by first attr type & value
##    elems = driver.find_elements(By.(eval(dic_args.items[0][0])), dic_args.items[0][1])
##
##    #for each element in list of elems, check if contains other attr type & value
##    for elem in elems:
##        if contains_attr_value(elem):
##            return elem
##
##    print('No element found')
##    return None
    
        


#point of these outside class is so can operate on elements

#to get element, supply initial tag, attribute type and name, eg id, 'abc'
#attribute value and list of more attribute types and names if want further attr info
#more_attrs should be list of tuples eg [ ('id','123'), ('name','jr') ]
def get_elem(element,initial_tag,attr_type=None,attr_name=None,more_attrs=None):
    try: 
        if not attr_type: #ie if searching by tag only
            return element.find_element_by_tag_name(initial_tag)
        else: #if searching via attributes as well
            #if not supplied xpath text, construct xpath from tag and attributes
            if not attr_type == 'xpath': attr_name = _construct_xpath_expr(initial_tag,attr_type,attr_name,more_attrs)
            attr_type = 'xpath'

            return element.find_element_by_xpath(attr_name)
    except: #if element not found
        print(f"Couldn't locate element Tag: {initial_tag}, Attribute: {attr_name}.")
        i=input('Try again. Enter any key to cancel retry')
        if not i:
            get_elem(element,initial_tag,attr_type,attr_name,more_attrs)

def get_elem_(element,attr_type,attr_name): #get element via attributes only
    try: 
        if attr_type=='id': return element.find_element_by_id(attr_name)
        elif attr_type=='class': return element.find_element_by_class_name(attr_name)
        elif attr_type=='name': return element.find_element_by_name(attr_name)
        elif attr_type=='link text': return element.find_element_by_link_text(attr_name)
        elif attr_type=='partial link text': return element.find_element_by_partial_link_text(attr_name)
        elif attr_type=='tag': return element.find_element_by_tag_name(attr_name)
        elif attr_type=='css': return element.find_element_by_css_selector(attr_name)
        elif attr_type=='xpath': return element.find_element_by_xpath(attr_name)
    except: #if element not found
        print(f"Couldn't locate element Attribute: {attr_name} of type: {attr_type}")
        i=input('Try again. Enter any key to cancel retry')
        if not i:
            get_elem_(element,attr_type,attr_name)
            


#get list of elements
def get_elems(element,initial_tag,attr_type=None,attr_name=None,more_attrs=None):
    try:
        if not attr_type: #ie if searching by tag only
            return element.find_elements_by_tag_name(initial_tag)
        else: #if searching via attributes as well
            #if not supplied xpath text, construct xpath from tag and attributes
            if not attr_type == 'xpath': attr_name = _construct_xpath_expr(initial_tag,attr_type,attr_name,more_attrs)
            attr_type = 'xpath'

        return element.find_elements_by_xpath(attr_name)
    except: #if element not found
        print(f"Couldn't locate elements Tag: {initial_tag}, Attribute: {attr_name}.")
        i=input('Try again. Enter any key to cancel retry')
        if not i:
            get_elems(element,initial_tag,attr_type,attr_name,more_attrs)


def get_elems_(element,attr_type,attr_name): #get elements via attributes only
    try: 
        if attr_type=='id': return element.find_elements_by_id(attr_name)
        elif attr_type=='class': return element.find_elements_by_class_name(attr_name)
        elif attr_type=='name': return element.find_elements_by_name(attr_name)
        elif attr_type=='link text': return element.find_elements_by_link_text(attr_name)
        elif attr_type=='partial link text': return element.find_elements_by_partial_link_text(attr_name)
        elif attr_type=='tag': return element.find_elements_by_tag_name(attr_name)
        elif attr_type=='css': return element.find_elements_by_css_selector(attr_name)
        elif attr_type=='xpath': return element.find_elements_by_xpath(attr_name)
    except: #if element not found
        print(f"Couldn't locate element Attribute: {attr_name} of type: {attr_type}")
        i=input('Try again. Enter any key to cancel retry')
        if not i:
            get_elems_(element,attr_type,attr_name)
            

def click_elem(element,initial_tag,attr_type=None,attr_name=None,more_attrs=None): #click on element
    try:
        get_elem(element,initial_tag,attr_type,attr_name,more_attrs).click()
    except: #if element not found
        print(f"Couldn't click element {initial_tag},{attr_name}.")
        i=input()
        if not i:
            click_elem(element,initial_tag,attr_type,attr_name,more_attrs)

def click_elem_(element,attr_type,attr_name): #click on element
    try:
        get_elem_(element,attr_type,attr_name).click()
    except: #if element not found
        print(f"Couldn't click element {attr_name}. To retry press enter else any other key to quit.")
        i=input()
        if not i:
            click_elem_(element,attr_type,attr_name)

def send_text(element,initial_tag,msg,attr_type=None,attr_name=None,more_attrs=None): #send msg to element
    try:
        get_elem(element,initial_tag,attr_type,attr_name,msg,more_attrs).send_keys(msg)
    except: #if element not found
        print(f"Couldn't send text: {msg} to element {initial_tag},{attr_name}.")
        i=input()
        if not i:
            send_text(element,initial_tag,attr_type,attr_name,msg,more_attrs)

def send_text_(element,attr_type,attr_name,msg): #send msg to element
    try:
        get_elem_(element,attr_type,attr_name).send_keys(msg)
    except: #if element not found
        print(f"Couldn't send text: {msg} to element {attr_name}.")
        i=input()
        if not i:
            send_text_(element,attr_type,attr_name,msg)

#WORK IN PROGRESS
##def send_text_slow(element,attr_type,attr_name,msg): #send msg to element slowly
##    try:
##        get_elem_(element,attr_type,attr_name).send_keys(msg)
##    except: #if element not found
##        print(f"Couldn't send text: {msg} to element {attr_name}.")
##        i=input()
##        if not i:
##            send_text_(element,attr_type,attr_name,msg)

def send_key(element,attr_type,attr_name,key): #send keys to element
    if key.lower()=='enter':
        send_text(element,attr_type,attr_name,Keys.ENTER)
    elif key.lower()=='down':
        send_text(element,attr_type,attr_name,Keys.DOWN)
    else:
        raise Exception(f'The key: {key} wasnt recognised')

def get_text(element):
    return element.text

def get_attr(element, attr):
    return element.get_attribute(attr)

def inner_html(element):
    return element.get_attribute('innerHTML')

def outer_html(element): #seems to work better
    return element.get_attribute('outerHTML')

def get_tag_names(element,include_descendents=False): #returns tag name of current element,
    #if include descendents, will get tag names for sub nodes as well
    if not include_descendents:
        return element.tag_name
    else:
        nodes = element.find_elements_by_xpath('descendant-or-self::*')
        result = []
        for node in nodes:
            result.append(current_tag(node))
        return result

def get_elements_with_tag(element,tag): #gets any current/sub webelements which have tag specified
    element.find_elements_by_xpath(f'descendant-or-self::{tag}')


def get_attrs(element,include_descendents=False): #returns attributes of current element,
    #if include descendents, will get attributes for sub nodes as well
    html = inner_html(element)
    print('Inner html: ',html)
    html = outer_html(element)
    print('Outer html: ',html)
    attrs = bs(html, 'html.parser').attrs
    return attrs
##    if not include_descendents:
##        return element.find_elements_by_xpath('attribute::*')
##    else:
##        nodes = element.find_elements_by_xpath('descendant-or-self::*')
##        result = []
##        for node in nodes:
##            result.append(current_tag(node))
##        return result
##    if attr:
##        return element.find_elements_by_xpath(f'attribute::{attr}')
##    else:

def select_item(element,attr_type,attr_name,list_item_txt):
    element=Select(get_elem_(element,attr_type,attr_name))
    element.select_by_visible_text(list_item_txt)

def item_checked(element,attr_type,attr_name):
    return get_elem_(element,attr_type,attr_name).is_selected()
        
    

#creates xpath expression from tag and attr type and name
def _construct_xpath_expr(tag,attr_type,attr_name,more_attrs):
    expr = f"//{tag}[@{attr_type}='{attr_name}']"
    if more_attrs:      
        for attr_type_name in more_attrs:
            expr  += f"[@{attr_type_name[0]}='{attr_type_name[1]}']"
    return expr


##def by_class(attr_type):
##    NOT WORKING*****
##    #eg input: 'name', output:By.NAME
##    dic={"id" : 'ID',  "xpath": 'XPATH', "link text":'LINK_TEXT',
##     "partial link text":'PARTIAL_LINK_TEXT', "name":'NAME',
##     "tag name":'TAG_NAME', "class name":'CLASS_NAME',
##     "css selector":'CSS_SELECTOR'}
##    try:
##        return list(By.__dict__.keys())[list(By.__dict__.values()).index('partial link text')]
##        print('here goes', dic[attr_type])
##        x=eval(f'By.{dic[attr_type]}')
##        print(type(x))
##        print('succesful')
##        return eval(f'By.{dic[attr_type]}')
##    except:
##        print(f"Couldn't find {attr_type}")
##        raise

 

class site:
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True

    
    def __formated_addr(self,site): #format webaddress so in right format
        if not re.match('http',site): #if doesn't start with http
            if re.match('www',site): #if starts with www
                return r'http:' + site #add http:\\
            else:
                return r'http://www.' + site #add http:\\www.....
        
        return site #if starts with http, address is ok

    def __init__(self,site,wait=5,headless=False):
        self.website = self.__formated_addr(site)
        options = Options()
        options.headless = headless
        self.driver = webdriver.Firefox(firefox_binary=binary,capabilities=self.cap, executable_path=gecko_path, options=options)
        self.driver.implicitly_wait(wait) #if happy to delay waiting for elements
        self.driver.get(self.website) #go to website

    def wait_conditional(self,attr_type,attr_value,max_time=5): #wait until item loaded
        #other conditions worth coding: element_to_be_clickable
        try:
            WebDriverWait(self.driver, max_time).until(EC.presence_of_element_located((attr_type, attr_value)))
        except excp.TimeoutException:
            print('Timeout. No element located')
        except Exception as e:
            print(type(e))
            print("Some other error locating element")


##    def get_elem(self,initial_tag,attr_type=None,attr_name=None,more_attrs=None): #get element
##        return get_elem(self.driver,initial_tag,attr_type,attr_name,more_attrs)

    def get_elem(self,attr_type,attr_name): #get element
        return get_elem_(self.driver,attr_type,attr_name)

    def get_elems(self,attr_type,attr_name): #get elements
        return get_elems_(self.driver,attr_type,attr_name)

    def click_elem(self,attr_type,attr_name): #click on element
        click_elem_(self.driver,attr_type,attr_name)
        
    def send_text(self,attr_type,attr_name,msg): #send msg to element
        send_text_(self.driver,attr_type,attr_name,msg)

    def send_key(self,attr_type,attr_name,key): #send key to element
        send_key(self.driver,attr_type,attr_name,key)

    def navigate(self,site):
        self.driver.get(site)

    def get_text(self):
        return get_text(self.driver)

    def get_tags(self,tag=None):
        return get_tags(self.driver,tag)

    def select_item(self,attr_type,attr_name,list_item_txt):
        select_item(self.driver,attr_type,attr_name,list_item_txt)

    def wait(self,secs):
        time.sleep(secs)
        
    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_no_frames(self): #unreliable i think
        return len(self.driver.find_elements_by_xpath("//iframe"))

    def switch_frame(self,frame_no=0,frame_name=None):
        self.driver.switch_to.default_content()
##        if not frame_name:
##            self.driver.switch_to_frame(frame_no)
##        else:
##            self.driver.switch_to_frame(frame_name)

    def parent_frame(self):
        self.driver.switch_to.parent_frame()

    def is_checked(self,attr_type,attr_name):
        return item_checked(self.driver,attr_type,attr_name)

    def screenshot(self,filepath):
        self.driver.get_screenshot_as_file(filepath)

    def screenshot_element(self,attr_type,attr_name,filepath): #screenshot of element
        self.get_elem_(attr_type,attr_name).screenshot(filepath)

    def screenshot_full(self,filepath): #fullpage screenshot
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
        self.driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
        self.driver.find_element_by_tag_name('body').screenshot(filepath)

    def current_webpage(self):####### look into this
        return self.driver.current_url
    
    def forward(self):####### look into this
        return self.driver.back()

    def back(self):####### look into this
        return self.driver.forward()

    def html(self):
        return self.driver.page_source

    def save(self,filepath):
        '''save current html to specified filepath'''
        with open(filepath, "w") as file:
            file.write(self.html())





##
##class elem:
##    dic={'id':element.find_element_by_id, 'class': element.find_element_by_class_name, 'name': element.find_element_by_name,
##        'link text': element.find_element_by_link_text, 'partial link text': element.find_element_by_partial_link_text,
##        'tag':element.find_element_by_tag_name, 'css':element.find_element_by_css_selector, 'xpath':element.find_element_by_xpath}
##
##
##    def __init__(self, attrs):
##        #find element by attribute given
##        for attr in attrs:
##            return dic[attr](attrs[attr])
##
##    def send_text(self,txt):
##        pass
##
##    def click(self):
##        pass
##
##
##class page:
##
##    cap = DesiredCapabilities().FIREFOX
##    cap["marionette"] = True
##
##    
##    def __formated_addr(self,site): #format webaddress so in right format
##        if not re.match('http',site): #if doesn't start with http
##            if re.match('www',site): #if starts with www
##                return r'http:' + site #add http:\\
##            else:
##                return r'http://www.' + site #add http:\\www.....
##        
##        return site #if starts with http, address is ok
##
##    def __init__(self,url,wait=5,headless=False):#navigate to webpage
##        self.website = self.__formated_addr(url)
##        options = Options()
##        options.headless = headless
##        self.driver = webdriver.Firefox(firefox_binary=binary,capabilities=self.cap, executable_path=gecko_path, options=options)
##        self.driver.implicitly_wait(wait) #if happy to delay waiting for elements
##        self.driver.get(self.website) #go to website
##
##
##    def get_elem(self, attrs):
##        #get element by attrs
##        return elem(attrs)
##
##    def get_elems(self, attrs):
##        #get element by attrs
##        pass
##
##    def switch_frame(self,frame=None):
##        pass
##
