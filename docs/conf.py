# Configuration file for the Sphinx documentation builder.

# -- Project information

# Jason added this 3pm 9/29/23 little block to debug broken images
# https://github.com/readthedocs/readthedocs.org/issues/1846#issuecomment-477184259
# import os
# if not os.path.exists('./git-lfs'):
#     os.system('wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.1/git-lfs-linux-amd64-v2.7.1.tar.gz')
#     os.system('tar xvfz git-lfs-linux-amd64-v2.7.1.tar.gz')
#     os.system('./git-lfs install')  # make lfs available in current repository
#     os.system('./git-lfs fetch')  # download content from remote
#     os.system('./git-lfs checkout')  # make local files to have the real content on them

project = 'Go-Kart'
copyright = '2023, XLAB '
author = 'XLAB'

release = '1.0'
version = '1.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'spinx_rtd_theme'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
