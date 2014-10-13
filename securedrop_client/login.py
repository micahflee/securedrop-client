import os, sys
from PyQt4 import QtCore, QtGui

import common

class Login(QtGui.QWidget):
    back_button_clicked = QtCore.pyqtSignal()
    
    def __init__(self, instance):
        super(Login, self).__init__()
        self.org = instance['org']
        self.landing_page = instance['landing_page']
        self.hs = instance['hs']
        
        # window title and icon
        self.setWindowTitle('SecureDrop')
        self.setWindowIcon(QtGui.QIcon(common.get_resource_path('securedrop.png')))
        
        # build the UI
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        
        # header label
        header = QtGui.QLabel(self.org)
        font = header.font()
        font.setPointSize(18)
        font.setBold(True)
        header.setFont(font)
        self.layout.addWidget(header)
        
        # landing page
        landing_page = QtGui.QLabel('<a href="{0}">Click for more information</a> about {1}\'s SecureDrop instance.'.format(self.landing_page, self.org))
        landing_page.setWordWrap(True)
        landing_page.setTextFormat(QtCore.Qt.RichText)
        landing_page.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        landing_page.setOpenExternalLinks(True)
        self.layout.addWidget(landing_page)
        
        # create account
        self.create_account_button = QtGui.QPushButton('Create Account')
        self.create_account_button.clicked.connect(self.create_account)
        
        create_account_group = QtGui.QGroupBox('Are you a new source?')
        create_account_layout = QtGui.QVBoxLayout()
        create_account_layout.addWidget(self.create_account_button)
        create_account_group.setLayout(create_account_layout)
        self.layout.addWidget(create_account_group)
        
        # login
        codename_layout = QtGui.QHBoxLayout()
        codename_label = QtGui.QLabel('Codename:')
        self.codename = QtGui.QLineEdit()
        codename_layout.addWidget(codename_label)
        codename_layout.addWidget(self.codename)
        
        self.login_button = QtGui.QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        
        login_group = QtGui.QGroupBox('Are you an existing source?')
        login_layout = QtGui.QVBoxLayout()
        login_layout.addLayout(codename_layout)
        login_layout.addWidget(self.login_button)
        login_group.setLayout(login_layout)
        self.layout.addWidget(login_group)
        
        # go back button
        self.back_button = QtGui.QPushButton('Choose a different organization')
        self.back_button.setStyleSheet('font-size:8pt;')
        self.back_button.clicked.connect(self.back_button_clicked.emit)
        self.layout.addWidget(self.back_button)
        
        self.show()

    def create_account(self):
        common.alert('Create account is not yet implemented.')
    
    def login(self):
        common.alert('Login is not yet implemented.')
