# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import suit_sortable

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = suit_sortable.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-suit-sortable',
    version=version,
    description='Drag-and-drop ordering for objects and inlines in Django admin using django-suit.',
    long_description=readme + '\n\n' + history,
    author='Mishbah Razzaque',
    author_email='mishbha@jp74.com',
    url='https://github.com/JP74/django-suit-sortable',
    packages=[
        'suit_sortable',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='suit_sortable',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
