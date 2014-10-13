import os, sys, tempfile, shutil, subprocess
from PyQt4 import QtCore, QtGui

import common
from choose_org import ChooseOrg
from login import Login

class ListVerificationFailed(Exception): pass

class Client(QtGui.QWidget):
    def __init__(self, app):
        super(Client, self).__init__()
        self.app = app
        
        self._load_securedrop_list()
        
        # open SecureDropList window
        self.choose_org = ChooseOrg(self.securedrop_list)
        self.choose_org.show()
        
        # launch login window
        self.choose_org.org_button_clicked.connect(self.launch_login)
        self.choose_org.other_button_clicked.connect(self.other_org)
    
    def launch_login(self, instance):
        self.login = Login(instance)
        self.login.back_button_clicked.connect(self.login_to_choose_org)
        self.choose_org.hide()
    
    def login_to_choose_org(self):
        self.login.close()
        self.choose_org.show()
    
    def other_org(self):
        common.alert('This has not been implemented yet. For now, choose one of the SecureDrop instances from the official list.')
    
    def _load_securedrop_list(self):
        # TODO: download securedrop_list.txt and securedrop_list.txt.asc from https://freedom.press/
        #       over Tor (or better yet, a hidden service) for updated list of instances
        
        # make a temporary gpg homedir and import securedrop pubkey
        homedir = tempfile.mkdtemp()
        subprocess.Popen(['/usr/bin/gpg', '--homedir', homedir, '--import', common.get_resource_path('securedrop.asc')]).wait()
        
        # verify the sig
        list_sig = common.get_resource_path('securedrop_list.txt.asc')
        p = subprocess.Popen(['/usr/bin/gpg', '--homedir', homedir, '--verify', list_sig])
        p.wait()
        if p.returncode != 0:
            shutil.rmtree(homedir)
            raise ListVerificationFailed
        
        # parse the list
        self.securedrop_list = []
        list_filename = common.get_resource_path('securedrop_list.txt')
        for line in open(list_filename, 'r').readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            
            org, landing_page, hs = line.split('\t')
            if org == 'Organization':
                continue
            
            self.securedrop_list.append({ 'org': org, 'landing_page': landing_page, 'hs': hs })
        
        # clean up temp files
        shutil.rmtree(homedir)

def main():
    app = QtGui.QApplication(sys.argv)
    client = Client(app)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
