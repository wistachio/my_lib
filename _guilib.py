from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class w:

    self.widget = None

    def __init__(self, name_widget,widget_arg=None,loc=None, size=None,
                 parent=None, signal=None,slot=None):
        '''
        widget: button/btn, tree, status bar, file sys, single text, txt box, tabs, msg box
        signal: click, sel changed, txt changed, current changed
        slot:
        '''
        '''Size: width,height'''

        if name_widget in ['button','btn']:
            self.widget = QPushButton()
        elif name_widget=='tree':
            self.widget=QTreeView()
        elif name_widget=='status bar':
            self.widget=QStatusBar()
        elif name_widget=='file sys':
            self.widget=QFileSystemModel()
        elif name_widget=='single text':
            self.widget=QLineEdit()
        elif name_widget=='txt box':
            self.widget=QTextEdit()
        elif name_widget=='tabs':
            self.widget=QTabWidget()       
        elif name_widget=='msg box':
            self.widget=QMessageBox()
        elif name_widget=='label':
            self.widget=QLabel()     


        if loc: self.loc(loc[0],loc[1])
        if size: self.size(size[0],size[1])

        if signal:
            if signal == 'click':
                signal = 'clicked'
            elif signal == 'sel changed':
                signal = 'selectionChanged'
            elif signal == 'txt changed':
                signal = 'textChanged'
            elif signal == 'current changed':
                signal = 'currentChanged'
                
            QObject.connect(widget, SIGNAL(signal), slot)

    def add(self, *widgets):
        for widget in widgets:
            self.widget.addWidget(widget)

    def size(width,height):
        pass

    def loc(x,y):
        pass

