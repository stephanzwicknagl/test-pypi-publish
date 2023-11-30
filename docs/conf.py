# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'viASP'
copyright = '2023, Stephan Zwicknagl, Luis Glaser'
author = 'Stephan Zwicknagl, Luis Glaser'

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
# sys.path.append(os.path.join(os.path.abspath(os.pardir)))
autodoc_mock_imports = ["clingo", "_clingo", "graphviz", "networkx", "viasp.shared", "viasp.wrapper"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx'
]
# intersphinx_mapping = {'clorm': ('https://clorm.readthedocs.io/en/latest/', None)}

# napoleon_google_docstring = False
# napoleon_use_ivar = True
napoleon_include_init_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_references = True

# napoleon_use_param = True
# napoleon_type_aliases = {
#     "Factbase": "clingraph.orm.Factbase",
#     "dict-like": ":term:`array-like`",
# }

# autodocs options
add_module_names = False
autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'canonical_url': '',
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']