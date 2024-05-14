import sphinx_rtd_theme
# https://www.sphinx-doc.org/en/master/usage/configuration.html


project = 'ddapi'
copyright = '2024, ByFox'
author = 'ByFox'
release = '3.2'

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = ["sphinx_rtd_theme",]
pygments_style = "sphinx"
version = '0.1.0'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
