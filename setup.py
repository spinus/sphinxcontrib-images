#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


setup(
    name='sphinxcontrib-images',
    version='0.4.2',
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
    install_requires=['sphinx>1.0',
                      'requests>2.2,<3'],
    namespace_packages=['sphinxcontrib'],
)
