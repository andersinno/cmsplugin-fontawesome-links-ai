# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='cmsplugin-fontawesome-links-ai',
    version='0.0.1',
    author='Anders Innovations',
    author_email='info@anders.fi',
    packages=find_packages(
        exclude=[
            "tests",
        ],
    ),
    include_package_data=True,
    license='MIT',
    long_description=open('README.rst').read(),
    description='Django CMS plugin for embedding links with fontawesome icons',
    install_requires=[
        'django-cms>=3.2,<3.5',
    ],
    url='https://github.com/andersinno/cmsplugin-fontawesome-links-ai',
)
