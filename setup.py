# -*- coding: utf-8 -*-
import os
import subprocess
from distutils.cmd import Command
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py


class FetchIconsYmlCommand(Command):
    description = 'Fetch icons.yml from Font-Awesome'

    yaml_url = 'https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml'
    static_path = 'cmsplugin_fontawesome_links_ai/static/cmsplugin_fontawesome_links_ai/yaml/icons.yml'
    command = 'curl {0} --create-dirs -o {1}'.format(yaml_url, static_path)

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        shell = (os.name == 'nt')
        subprocess.check_call(self.command.split(), shell=shell)


class BuildStaticResourcesCommand(Command):
    description = 'Build static resources with npm'
    command = 'npm run build'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        shell = (os.name == 'nt')
        subprocess.check_call(self.command.split(), shell=shell)


class BuildPyCommand(build_py):

    def run(self):
        self.run_command('fetch_icons')
        self.run_command('npm_build')
        build_py.run(self)


setup(
    name='cmsplugin-fontawesome-links-ai',
    version='0.0.1',
    author='Anders Innovations',
    author_email='info@anders.fi',
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    license='MIT',
    long_description=open('README.rst').read(),
    cmdclass={
        'fetch_icons': FetchIconsYmlCommand,
        'npm_build': BuildStaticResourcesCommand,
        'build_py': BuildPyCommand,
    },
    description='Django CMS plugin for embedding links with fontawesome icons',
    install_requires=[
        'pyyaml>=3.0',
        'django-cms>=3.2,<3.5',
    ],
    url='https://github.com/andersinno/cmsplugin-fontawesome-links-ai',
)
