# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = '银色子弹'
copyright = '2020, Shengyu Zhang'
author = 'Shengyu Zhang'

# -- Non-standard project information ----------------------------------------

description = 'Yes silver bullet here.'
baseurl = 'https://silverrainz.me'
datefmt = '%Y-%m-%d'

# -- Configuration item Initialization ---------------------------------------

extensions = []
html_sidebars = {}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions += [
    'sphinx.ext.graphviz',
    'sphinxcontrib.email',
    'sphinxnotes.lilypond',
    'sphinx.ext.githubpages',
    'sphinx_panels',
    'sphinx.ext.intersphinx',
    'sphinxnotes.strike',
]

extensions += ['sphinx.ext.todo']
todo_include_todos = True

extensions += ['sphinx.ext.extlinks']
extlinks = {
    'zhwiki': ('https://zh.wikipedia.org/wiki/%s', ''),
    'enwiki': ('https://wikipedia.org/wiki/%s', ''),
    'search': ('https://duckduckgo.com/?q=%s', ''),
    'twitter': ('https://twitter.com/%s', '@'),
    'github': ('https://github.com/%s', '@'),
    'weibo': ('https://weibo.com/%s', '@'),
}

extensions += ['sphinx.ext.autosectionlabel']
autosectionlabel_prefix_document = True

extensions += ['sphinxnotes.any']
any_predefined_schemas = []
any_custom_schemas = [{
        'type': 'friend',
        'fields': {
            'others': ['avatar', 'blog'],
        },
        'templates': {
            'reference': '@{{ title }}',
            'content': """
{% if avatar %}
.. image:: {{ avatar }}
   :width: 120px
   :alt: {{ names[0] }}
   :align: right
{% endif %}

{{ blog }}

{{ content | join('\n') }}"""
        }
},{
    'type': 'book',
     'fields': {
         'id': 'isbn',
         'others': ['cover', 'status', 'startat'],
     },
     'templates': {
         'reference': '《{{ title }}》',
         'content': """
:ISBN: {{ isbn }}

{{ content | join('\n') }}"""
     }
},{
    'type': 'artworks',
     'fields': {
         'id': 'id',
         'others': ['date', 'medium', 'size', 'image'],
     },
     'templates': {
         'reference': '《{{ title }}》',
         'content': """
:id: {{ id }}
:date: {{ date }}
:size: {{ size }}
:medium: {{ medium }}

{{ content | join('\n') }}"""
     }
}]

extensions += ['ablog']
blog_path = 'blog'
blog_title = project
blog_baseurl = baseurl
blog_authors = {
    'LA': ('Shengyu Zhang', blog_baseurl),
}
blog_default_author = 'LA'
blog_languages = {
    'zh': ('Chinese', None),
    'en': ('English', None),
}
blog_default_language = 'zh'
post_date_format = datefmt
post_auto_image = 1
blog_feed_fulltext = True
blog_feed_subtitle = description

extensions += ['sphinxcontrib.gtagjs']
gtagjs_ids = [ 'G-FYHS50G6DL' ]

extensions += ['sphinxnotes.khufu.ext.snippet']
khufu_snippet_patterns = ['man/.*']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Provided by sphinxnotes.any
primary_domain = 'any'

# Use :code: as default role, so we can write `content` instead of ``content``.
default_role = 'code'

# Auto numbered figures, tables and code-blocks if they have a caption.
numfig = True

# Show codeauthor and sectionauthor directives produce any output in the built
# files.
show_authors = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': project,
    'description': description,
    'touch_icon': 'logo.png',
    'page_width': '80%',
}

html_sidebars = {
    # Match all blog pages
    'blog/*': [
        'about.html', 'postcard.html', 'recentposts.html',
        'tagcloud.html', 'categories.html', 'archives.html',
    ],
    # Match all pages but excluding blog
    '*[!blog]*': [
        'about.html', 'navigation.html', 'relations.html',
        'searchbox.html', 'donate.html',
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['center-title.css', 'ablog.css']

html_baseurl = baseurl

html_title = project

# If true, the reST sources are included in the HTML build as _sources/name.
# I don't want to public my sources, so set it to false.
html_copy_source = False

html_search_language = 'zh'

html_favicon = '_static/favicon.png'
