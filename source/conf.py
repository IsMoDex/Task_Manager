# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../program/financial_operations'))
sys.path.insert(0, os.path.abspath('../program/innovative_technologies'))
sys.path.insert(0, os.path.abspath('../program/task_management'))

project = 'Task Manager'
copyright = '2025, Modex'
author = 'Modex'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Для автогенерации документации из docstrings
    'sphinx.ext.napoleon',  # Для поддержки Google и NumPy стилей docstrings
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
