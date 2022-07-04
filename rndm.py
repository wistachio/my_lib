import random as r
import string

punc = '!£$&*@#~?_-' #string of punctuations to u

def rand_no(_type='real', lower_bound='any', upper_bound='any'):
    
    if lower_bound=='any': lower_bound=-10000 #initialise bounds
    if upper_bound=='any': upper_bound=10000
    
    if _type.lower()=='real':
        return r.uniform(lower_bound,upper_bound)
    elif _type.lower() =='int':
        return r.randint(lower_bound,upper_bound)
        

def rand_str(length='random'):
    '''return a lowercase string of length specified, default is random'''
    if length=='random': length=rand_no(_type='int',lower_bound=1)
    return ''.join([x for y in range(length) for x in r.choice(string.ascii_lowercase)])


def str_generator(min_size=8,max_size=16,
                  include_upper=True, include_punc=True, include_digits=True,
                  min_upper=False, min_punc=False, min_digit=False):
    '''generates random string
    can specify:
    if want random uppercase, punctuation, digits in string: include_upper etc
    if require at least 1 uppercase, punctuation, digits: min_upper etc
    NOTE:can use str_generator(2,6) to give string between 2-6
    Eg
    str_generator(6,6,min_punc=True,include_punc=False)
    will give string of lenght 6, with only 1 punctuation
    '''
    output = '' #initialise output
    
    chars=string.ascii_lowercase
    if include_upper: chars=string.ascii_letters #if want upper case chars too
    if include_punc: chars+=punc
    if include_digits: chars+= string.digits 
    
    size=rand_no(_type='int',lower_bound=min_size, upper_bound=max_size)#set size to value between upper/lower
    if min_upper:
        min_upper=r.choice(string.ascii_uppercase)
        output+=min_upper
        size-=1 #decrease size to account for upper
    if min_punc:
        min_punc=r.choice(punc)
        output+=min_punc
        size-=1
    if min_digit:
        min_digit=r.choice(string.digits)
        output+=min_digit
        size-=1
        
    return ''.join(r.choice(chars) for _ in range(size)) + output
    
