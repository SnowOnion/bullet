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
author = 'Shengyu Zhang'
author_id = 'SilverRainZ'
author_nick = 'LA'
copyright = '2020-2021, ' + author

# -- Non-standard project information ----------------------------------------

logo = '_static/logo.png'
description = 'Yes silver bullet here.'
baseurl = 'https://silverrainz.me/'
datefmt = '%Y-%m-%d'

# -- Enviroment information -----------------------------------------------------

CI = os.environ.get('CI') is not None

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.graphviz',
    'sphinxcontrib.email',
    'sphinx.ext.githubpages',
    'sphinxnotes.strike',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.asciinema',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'
language_full = '简体中文'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Provided by sphinxnotes.any
primary_domain = 'any'

# Use :code: as default role, so we can write `content` instead of ``content``.
default_role = 'code'

# Keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
if not CI:
    keep_warnings = True

# Auto numbered figures, tables and code-blocks if they have a caption.
# numfig = True

# Show codeauthor and sectionauthor directives produce any output in the built
# files.
show_authors = True

# A URL to cross-reference manpage directives.
manpages_url = 'https://linux.die.net/man/{section}/{page}'

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

html_baseurl = baseurl

html_title = project

# html_logo = logo

html_favicon = '_static/favicon.png'

# HTML theme configuration
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': False,
    'touch_icon': 'logo.png',
    'description': description,
    'page_width': '80%',
}
html_css_files.append('alabaster-custom.css')

nosidebar_page = ['nosidebar.html']
standard_page = ['about.html', 'localtoc.html', 'searchbox.html']
blog_post_page = ['about.html', 'postcard.html', 'localtoc.html',
                  'recentposts.html', 'tagcloud.html', 'categories.html',
                  'archives.html', 'searchbox.html']
# TODO...

html_sidebars = {
    # We have best toc on page content
    'about/resume': nosidebar_page,
    'about/resume-en': nosidebar_page,
    'blog': blog_post_page, # ABlog's "All Posts" page
    'blog/**': blog_post_page, # Inlucde posts and autogenerated pages
}

# If true, the reST sources are included in the HTML build as _sources/name.
# I don't want to public my sources, so set it to false.
html_copy_source = False

html_search_language = language

html_last_updated_fmt = datefmt

# A list of paths that contain extra files not directly related to the
# documentation.
html_extra_path = ['robots.txt']

# -- Pre extension configuration ---------------------------------------------------

extensions.append('sphinx.ext.todo')
todo_include_todos = True

extensions.append('sphinx.ext.extlinks')
extlinks = {
    'zhwiki': ('https://zh.wikipedia.org/wiki/%s', '📖'),
    'enwiki': ('https://wikipedia.org/wiki/%s', '📖'),
    'search': ('https://duckduckgo.com/?q=%s', '🔍'),
    'twitter': ('https://twitter.com/%s', '👤'),
    'ghuser': ('https://github.com/%s', '👤'),
    'ghorg': ('https://github.com/%s', '👥'),
    'ghrepo': ('https://github.com/%s', '⛺'),
    'weibo': ('https://weibo.com/%s', '👤'),
    'aur': ('https://aur.archlinux.org/packages/%s', '📦'),
    'archpkg': ('https://archlinux.org/packages/%s', '📦'),
    'archwiki': ('https://wiki.archlinux.org/index.php/%s', '📖'),
    'zhihuq': ('https://www.zhihu.com/question/%s', '❓'),
    'zhihua': ('https://www.zhihu.com/answer/%s', '❓'),
    'zhihup': ('https://www.zhihu.com/people/%s', '👤'),
    'pypi': ('https://pypi.org/project/%s', '📦'),
    'lilydoc': ('https://lilypond.org/doc/v2.20/Documentation/%s', 'https://lilypond.org/doc/v2.20/Documentation/'),
}

extensions.append('sphinxnotes.any')
from sphinxnotes.any import Schema, Field as F
any_schemas = [
    Schema('friend',
           name=F(unique=True, referenceable=True, required=True, form=F.Form.LINES),
           attrs={'avatar': F(), 'blog': F()},
           description_template=open('_templates/friend.rst', 'r').read(),
           reference_template='👤{{ title }}',
           missing_reference_template='👤{{ title }}',
           ambiguous_reference_template='👥{{ title }}'),
    Schema('book',
           name=F(required=True, referenceable=True, form=F.Form.LINES),
           attrs={
               'isbn': F(unique=True, referenceable=True),
               'status': F(referenceable=True),
               'startat': F(referenceable=True, form=F.Form.WORDS),
               'endat': F(referenceable=True, form=F.Form.WORDS),
           },
           description_template=open('_templates/book.rst', 'r').read(),
           reference_template='《{{ title }}》',
           missing_reference_template='《{{ title }}》',
           ambiguous_reference_template='《{{ title }}》'),
    Schema('artwork',
           name=F(referenceable=True),
           attrs={
               'id': F(unique=True, referenceable=True, required=True),
               'date': F(referenceable=True),
               'medium': F(referenceable=True, form=F.Form.WORDS),
               'size': F(referenceable=True),
               'image': F(),
               'album': F(referenceable=True),
           },
           description_template=open('_templates/artwork.rst', 'r').read(),
           reference_template='《{% if title %}{{ title }}{% else %}{{ id }}{% endif %}》',
           missing_reference_template='《{{ title }}》',
           ambiguous_reference_template='{{ title }}'),
    Schema('artist',
           name=F(unique=True, referenceable=True, required=True, form=F.Form.LINES),
           attrs={'movement': F(referenceable=True, form=F.Form.WORDS)},
           description_template=open('_templates/artist.rst', 'r').read(),
           reference_template='👤{{ title }}',
           missing_reference_template='👤{{ title }}',
           ambiguous_reference_template='👥{{ title }}'),
    Schema('gallery',
           name=F(unique=True, referenceable=True, required=True, form=F.Form.LINES),
           attrs={'website': F()},
           description_template=open('_templates/gallery.rst', 'r').read(),
           reference_template='🖼️{{ title }}',
           missing_reference_template='🖼️{{ title }}'),
    Schema('event',
           name=F(referenceable=True, required=True),
           attrs={
               'date': F(referenceable=True, form=F.Form.LINES),
               'location': F(referenceable=True),
           },
           description_template=open('_templates/event.rst', 'r').read(),
           reference_template='📅{{ title }}',
           missing_reference_template='📅{{ title }}',
           ambiguous_reference_template='📅{{ title }}'),
    Schema('leetcode',
           name=F(referenceable=True, required=True),
           attrs={
               'id': F(unique=True, referenceable=True),
               'diffculty': F(referenceable=True),
               'language': F(referenceable=True, form=F.Form.WORDS),
               'key': F(referenceable=True, form=F.Form.WORDS),
               'date': F(referenceable=True, form=F.Form.WORDS),
               'reference': F(referenceable=True),
           },
           description_template=open('_templates/leetcode.rst', 'r').read(),
           reference_template='🧮{{ title }}',
           missing_reference_template='🧮{{ title }}',
           ambiguous_reference_template='🧮{{ title }}'),
]

extensions.append('ablog')
blog_path = 'blog'
blog_title = project
blog_baseurl = baseurl
blog_authors = {
    author_nick: (author, blog_baseurl),
}
blog_default_author = author_nick
blog_languages = {
    language: (language_full, None),
    'en':     ('English',  None),
}
blog_default_language = language
post_date_format = datefmt
post_auto_image = 1
blog_feed_fulltext = True
blog_feed_subtitle = description
fontawesome_included = True
html_css_files.append('ablog.css')

if CI:
    extensions.append('sphinxcontrib.gtagjs')
    gtagjs_ids = ['G-FYHS50G6DL']

if not CI:
    extensions.append('sphinxnotes.snippet.ext')
    snippet_config = {}
    snippet_patterns = {
        'd': ['.*'],
        's': ['man/.*', 'notes/.*', 'misc/.*'],
        'c': ['man/.*'],
    }

extensions.append('sphinx_panels')
if CI:
    # For ``fa`` role
    html_css_files.append('https://cdn.bootcdn.net/ajax/libs/font-awesome/5.15.2/css/all.css')

extensions.append('sphinxnotes.isso')
isso_url = 'https://comments.silverrainz.me:30500'

if CI:
    extensions.append('sphinx_sitemap')
    sitemap_filename = "sitemap.xml"
    sitemap_url_scheme = "{link}"

if CI:
    extensions.append('sphinx.ext.intersphinx')
    intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
        'sphinx': ('https://www.sphinx-doc.org/en/stable/', None),
        'srain': ('https://srainapp.github.io/docs', None),
    }

    extensions.append('sphinx_reredirects')
    # https://documatt.gitlab.io/sphinx-reredirects/usage.html
    redirects = {
        # '<docname>': '<html/url>'
        'notes/srain': 'https://srainapp.github.io/docs/arch/index.html',
    }

# extensions.append('sphinxcontrib.images')
# images_config = {
#     'override_image_directive': True,
#     'cache_path': '_cache',
#     'download': True,
# }

extensions.append('sphinxnotes.lilypond')
lilypond_audio_volume = 300
