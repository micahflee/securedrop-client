import os, sys
from PyQt4 import QtCore, QtGui

import common

class ChooseOrg(QtGui.QWidget):
    org_button_clicked = QtCore.pyqtSignal(dict)
    other_button_clicked = QtCore.pyqtSignal()
    
    def __init__(self, securedrop_list):
        super(ChooseOrg, self).__init__()
        self.securedrop_list = securedrop_list
        
        # window title and icon
        self.setWindowTitle('SecureDrop')
        self.setWindowIcon(QtGui.QIcon(common.get_resource_path('securedrop.png')))
        
        # build the UI
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QtGui.QLabel('Choose an organization:')
        self.layout.addWidget(self.label)
        
        # organization buttons
        self.buttons = {}
        for instance in self.securedrop_list:
            # make a function that emits org_button_clicked with the right instance
            org_button_clicked = self.org_button_clicked
            def make_func(instance):
                def func():
                    org_button_clicked.emit(instance)
                return func
            
            # function to call when button is clicked
            func = make_func(instance)
            
            button = QtGui.QPushButton(instance['org'])
            button.clicked.connect(func)
            self.layout.addWidget(button)
            
            self.buttons[instance['org']] = button
        
        # the other button
        self.other_button = QtGui.QPushButton('Other...')
        self.other_button.clicked.connect(self.other_button_clicked.emit)
        self.layout.addWidget(self.other_button)

