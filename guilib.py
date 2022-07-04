from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re

def _tokeniser(inp):
    '''returns no of rows, how to set up each
    eg: 3 buttons, 2 txtboxes
    2 buttons(names:'b1','b2'), txtbox
    2 textboxes, 1 button, r2: 4 textboxes(options=...)'''
    
    pattern = r'(?P<row>\d*(?=[:]))[:]*\s*(?P<no>\d*)\s*(?P<widget>[a-z]+)[(]?(?P<options>[a-zA-Z0-9_=:-£$#]*)[)]?[,]?\s?' # pattern = number? widdget (options?)
    #pattern = r'(\d+(?=[:]))([:]+\s+)(\d+)'#\s*[a-z]*'
    pattern = r'\d*[:]*'#(\s*)(\d*)'
    p1 = r'\d+[:]\s*'
    p2 = r'(\b\d+\b)\s*'
    p3 = r'(?<![(])\b[a-z]+\b(?![)])\s*'
    p4 = r'[(]{1}([a-zA-Z0-9_=:-£$#.,]*)[)]{1}\s*' 
    reg = re.compile('('+p1+')*('+p2+')*('+p3+'){1}('+p4+')*')
    return reg.findall(inp)

class gui:
    def __init__(self,loc=(1900, 50),size=(1900, 2150)):  
        self.qapp = QApplication([])
        self.window = QWidget()

        a,b,c,d=(loc+size)
        self.window.setGeometry(QRect(a,b,c,d))

    def end(self,widget):

        self.window.setLayout(widget)
        
        self.window.show()
        self.qapp.exec_()

    def button(self,txt='',size=None,loc=None,events={}):
        _ = QPushButton()
        if txt: _.setText(txt)
        if events:
            for event in events:
                eval(f'_.{event}.connect({events[event]}')
        return _

    def _txtbox(self):
        #internal method for both type of text boxes
        pass

    def msgbox(self,msg):
        _ = QMessageBox()
        _.setText(msg)
        _.exec()

    def msgbox_input(self,title=None,label=None,default_value=None,ok=None,cancel=None):
        cancel, ok = QInputDialog.getText(QInputDialog(), title, label, QLineEdit.Normal, default_value) #input msgbox
        #if supplied functions to do stuff on ok,cancel
        if ok: ok()
        if cancel: cancel()
            

    def splitter(self,horiz=True,size=(400,400),loc=None,widgets=[]):
        _ = QSplitter()
        if not horiz:
            _ = QSplitter(Qt.Vertical) #splitter orientation, default is horizon
        
        for widget in widgets:
            _.addWidget(widget)
            
        _.setSizes(list(size))

        return _

    def tree(self,direc,size=(400,400),loc=None,events={},options={}):
        pass

    def panel(self,horiz=True,size=None,loc=None,widgets=[]):
        _ = QVBoxLayout()
        if horiz:
            _=QHBoxLayout()

        for widget in widgets:
            _.addWidget(widget)

##        __ = QWidget() #create temp widget
##        __.setLayout(_)

        return _

    

##g=gui()
##
###m = g.msgbox('jibrannnnnn')
##m2 = g.msgbox_input()
##but1 = g.button('hello')
##but2 = g.button()
##spl1 = g.splitter(widgets=[but1,but2])
##p = g.panel(widgets=[spl1])
##
##g.end(p)


a = '3 buttons, 2 txtboxes'
b = '2 buttons(names:b1,b2), txtbox'
c = '2 textboxes, 1 button, r2: 4 textboxes(options=...)'
c = 'r2: 4 textboxes(options=...)'
lst = [a,b,c]

for x in lst:
    t=_tokeniser(x)
    for _ in t:
        print(_)
    print(x, '\n', len(t[0]),'\n', t,'\n')
