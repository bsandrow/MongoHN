from __future__ import print_function

from glob import glob

try:
    from setuptools import setup
except ImportError:
    print("Falling back to distutils. Functionality may be limited.")
    from distutils.core import setup

requires = []
long_description = open('README.rst').read() + "\n\n" + open("ChangeLog").read()

config = {
    'name'            : 'MongoHN',
    'description'     : 'A HackerNews-clone with a MongoDB backend.',
    'long_description': long_description,
    'author'          : 'Brandon Sandrowicz',
    'author_email'    : 'brandon@sandrowicz.org',
    'url'             : 'https://github.com/bsandrow/mongohn',
    'version'         : '0.1',
    'packages'        : ['mongohn'],
    'package_data'    : { '': ['LICENSE'] },
    'scripts'         : glob('bin/*'),
    'install_requires': requires,
    'license'         : open('LICENSE').read(),
    'test_suite'      : 'mongohn.tests',
}

setup(**config)
