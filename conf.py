# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'FRC CNC Pathing'
copyright = '2022, Everen Wegner'
author = 'Everen Wegner'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autosectionlabel', 'sphinx.ext.todo', 'sphinxcontrib.images',]

# Display todos by setting to True
todo_include_todos = True

# Configure image defaults
images_config = {'default_image_width': 'auto', 'default_image_height': 'auto', 'show_caption': True, 'align': 'center'}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
 
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static/sphinx_rtd_theme']