#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import tox
        errno = tox.cmdline()
        sys.exit(errno)


setup(
    name='sphinxcontrib-images',
    version='0.5.0',
    url='https://github.com/spinus/sphinxcontrib-images',
    download_url='https://pypi.python.org/pypi/sphinxcontrib-images',
    license='Apache 2',
    author=u'Tomasz Czyż',
    author_email='tomasz.czyz@gmail.com',
    description='Sphinx "images" extension',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Documentation',
    ],
    entry_points={
        'console_scripts':[
            'sphinxcontrib-images=sphinxcontrib.images:main',
        ],
        'sphinxcontrib.images.backend':[
            'LightBox2 = sphinxcontrib_images_lightbox2:LightBox2',
            'FakeBackend = sphinxcontrib_images_lightbox2:LightBox2',
        ]
    },
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['wheel'],
    install_requires=['sphinx>=1.1.3,<2',
                      'requests>2.2,<3'],
    tests_require=['tox==1.8.1'],
    cmdclass = {'test': Tox},
    namespace_packages=['sphinxcontrib'],
)
