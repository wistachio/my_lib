import re

class gen:
    def __init__(self, element):
        stripped_element = element.strip('<').strip('>')
        tag= stripped_element.split(' ')[0]
        attrs = stripped_element.lstrip(tag+' ')
