#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requirements=[
    'django-crispy-forms>=1.4.0',
    'Django>=1.7.0',
    'bleach>=1.4.2',
    'python-dateutil>=2.5.3',
    'future>=0.16'
]

setup(
    name='ai-django-core',
    version='1.1.2',
    author=u'Ambient Innovation GmbH',
    author_email='info@ambient-innovation.com',
    packages=find_packages(),
    include_package_data=True,
    url='ssh://git@gitlab.ambient-innovation.com:20141/ai/ai-django-core',
    license='BSD License',
    description='Lots of helper functions and useful widgets.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    dependency_links = ['https://github.com/ambient-innovation/multiav/master/#egg=multiav',],
    install_requires=requirements
)
