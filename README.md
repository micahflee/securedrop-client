# SecureDrop Client

A desktop client for SecureDrop. *This software is under development and isn't done yet. Don't try using it.*

## Install

```sh
sudo apt-get install build-essential fakeroot python-all python-stdeb python-qt4 gnupg tor
git clone https://github.com/micahflee/securedrop-client.git
cd securedrop-client
./build_deb.sh
sudo dpkg -i deb_dist/securedrop-client_*.deb
```
