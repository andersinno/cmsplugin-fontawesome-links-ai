==============================
cmsplugin-fontawesome-links-ai
==============================

Django CMS plugin for embedding links with fontawesome icons


This plugin is based on `django-fontawesome <https://github.com/redouane/django-fontawesome>`_ plugin.

Requirements
------------

- PyYAML (``pip install pyyaml``)

Inbuilt commands
----------------

1. ``python setup.py fetch_icons``

Fetches the most current version of icons.yml from Font-Awesome.

2. ``python setup.py npm_build``

Installs bower and gulp locally, then runs them to fetch and compile static css, js and fonts files.

3. ``python setup.py build_py``

Customized ``build_py`` command that includes ``fetch_icons`` and ``npm_build``

Font-Awesome version
--------------------

Current version is 4.7.0

``python setup.py fetch_icons``, ``python setup.py build_py`` or ``python setup.py bdist_wheel`` would all fetch the
newest Font-Awesome version.

Getting started
---------------

1. Install
2. Add ``'cmsplugin_fontawesome_links_ai'`` to ``INSTALLED_APPS``
3. Implement frontend

- This package includes only a reference template (``templates/cmsplugin_fontawesome_links_ai/fontawesome_links.html``).
- This package does not include any styling.

Installing for development
--------------------------

Use ``pip install -e /path/to/checkout`` to install as "editable" package to your venv
