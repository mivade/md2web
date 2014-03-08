#!/usr/bin/env python
"""
md2web.py

Script for compiling markdown documents into HTML.

"""

from __future__ import print_function
from __future__ import unicode_literals
import os.path
import glob
import re
import argparse
import markdown

# Configuration
# -------------

# This is the template file to use. This allows for common elements
# across all pages. This can be overridden with the command line
# argument --template.
DEFAULT_TEMPLATE_FILE = "template.html"

# File extensions that signify Markdown files.
_FILE_EXTENSIONS = ["md", "markdown", "mkd", "mdown", "text"]

# Markdown extensions to use.
md_extensions = ["extra", "codehilite", "meta", "wikilinks", "latex"]

# Functions
# ---------

def init_cli_args():
    """Setup command line options. Returns an ArgumentParser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template", default=DEFAULT_TEMPLATE_FILE,
        help="HTML template file to use for conversion. Defaults to " \
        + DEFAULT_TEMPLATE_FILE)
    parser.add_argument(
        "--base-url", default="",
        help="Base URL to replace $ROOT in the template file. " + \
        "Useful for specifying site-wide CSS file locations, for example." + \
        " Defaults to ''. This assumes the trailing / is in the " + \
        "template file and so strips any trailing / character from " + \
        "the option.")
    parser.add_argument(
        "--no-template", action="store_true",
        help="Don't use a template file.")
    parser.add_argument(
        "markdown_file", nargs=1, default="__DIR__",
        help="The Markdown file to convert to HTML.")
    return parser

def convert(filename, base_url, template_filename=None):
    """
    Compile the Markdown file filename into HTML.

    Parameters
    ----------
    filename : str
        Filename of the Markdown file to convert to HTML.
    base_url : str
        Base URL to find/replace $ROOT in the template file.
    template_file : str or None, optional
        If a str, specifies the template file to use when converting
        to HTML.

    """
    output_filename = filename.split('.')[0] + '.html'
    md = markdown.Markdown(extensions=md_extensions, output_format="xhtml1")
    with open(filename, 'r') as md_file:
        md_text = md_file.read()
        html = md.convert(md_text)
    try:
        title = md.Meta['title'][0]
    except KeyError:
        title = md_text.split('\n')[0].strip()
    if template_filename:
        with open(template_filename, 'r') as template_file:
            template = template_file.read()
        try:
            if base_url[-1] == '/':
                base_url = base_url[:-1]
        except IndexError:
            pass
        template = re.sub("\$TITLE", title, template)
        template = re.sub("\$ROOT", base_url, template)
        template = re.sub("\$CONTENT", html, template)
        html = template
    with open(output_filename, 'w') as output_file:
        output_file.write(html)

# Main
# ----

if __name__ == "__main__":
    parser = init_cli_args()
    args = vars(parser.parse_args())
    if args['no_template']:
        args['template'] = None
    convert(args['markdown_file'][0], args['base_url'], args['template'])
