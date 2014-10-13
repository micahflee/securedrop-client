import os, sys, platform

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()

setup(
    name='securedrop-client',
    version=version,
    author='Micah Lee',
    author_email='micah@freedom.press',
    platforms=['GNU/Linux'],
    license='GPLv3',
    description='Desktop client for SecureDrop',
    long_description="""
Desktop client for SecureDrop
    """,
    packages=['securedrop_client'],
    include_package_data=True,
    scripts=['securedrop-client'],
    data_files=[
        (os.path.join(sys.prefix, 'share/applications'), ['install/securedrop-client.desktop']),
        (os.path.join(sys.prefix, 'share/pixmaps'), ['install/securedrop-client.xpm']),
        (os.path.join(sys.prefix, 'share/securedrop-client'), [
            'share/securedrop.asc',
            'share/securedrop.png',
            'share/securedrop_list.txt',
            'share/securedrop_list.txt.asc'
        ]),
    ]
)
