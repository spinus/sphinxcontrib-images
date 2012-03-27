#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# tested only with it, if you tested with older version and it worked, pleas
# let me know
requires = ['Sphinx>=0.9'] 

setup(
    name='sphinxcontrib-fancybox',
    version='0.1',
    url='http://github.com/spinus/sphinxcontrib-fancybox',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-fancybox',
    license='BSD',
    author=u'Tomek Czyż',
    author_email='tomekczyz@gmail.com',
    description='Sphinx "fancybox" extension',
    long_description=open(os.path.join(
                              os.path.dirname(__file__),
                              'readme.rst')
                         ).read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
