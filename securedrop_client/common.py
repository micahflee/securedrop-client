# -*- coding: utf-8 -*-
import os, sys
from PyQt4 import QtGui

def get_resource_path(filename):
    prefix = os.path.join(sys.prefix, 'share/securedrop-client')
    return os.path.join(prefix, filename)

def alert(message, icon=QtGui.QMessageBox.NoIcon):
    dialog = QtGui.QMessageBox()
    dialog.setWindowTitle("SecureDrop")
    dialog.setWindowIcon(QtGui.QIcon(get_resource_path('securedrop.png')))
    dialog.setText(message)
    dialog.setIcon(icon)
    dialog.exec_()
