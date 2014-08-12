#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""md2web

A simple script for compiling markdown documents into HTML.

"""

from __future__ import print_function
import argparse
import jinja2
import markdown

# Configuration
# =============================================================================

# File extensions that signify Markdown files.
_FILE_EXTENSIONS = ["md", "markdown", "mkd", "mdown", "text"]

# Markdown extensions to use.
md_extensions = ["extra", "codehilite", "meta", "wikilinks"]

# Functions
# =============================================================================

def init_cli_args():
    """Setup command line options. Returns an ArgumentParser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-url", default="",
        help="Base URL to replace $ROOT in the template file. " + \
        "Useful for specifying site-wide CSS file locations, for example." + \
        " Defaults to ''. This assumes the trailing / is in the " + \
        "template file and so strips any trailing / character from " + \
        "the option.")
    parser.add_argument(
        "--template", default='',
        help="Jinja2 template file to use for conversion.")
    parser.add_argument(
        "--no-template", action="store_true",
        help="Don't use a template file.")
    parser.add_argument(
        "markdown_file", nargs=1, default="__DIR__",
        help="The Markdown file to convert to HTML.")
    return parser

def convert(filename, base_url, template_filename=None):
    """Compile the Markdown file filename into HTML.

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
    # Process markdown file
    output_filename = filename.split('.')[0] + '.html'
    md = markdown.Markdown(extensions=md_extensions, output_format="html5")
    with open(filename, 'r') as md_file:
        md_text = md_file.read()
        content = md.convert(md_text)
    try:
        title = md.Meta['title'][0]
    except KeyError:
        title = md_text.split('\n')[0].strip()

    # Load template file
    if template_filename is not None:
        with open(template_filename, 'r') as template_file:
            template = jinja2.Template(template_file.read())
        try:
            if base_url[-1] == '/':
                base_url = base_url[:-1]
        except IndexError:
            pass

        # Render the template with the content
        html = template.render(title=title, content=content, root=base_url)
    else:
        html = content

    # Output HTML
    with open(output_filename, 'w') as output_file:
        output_file.write(html)

# Main
# =============================================================================

if __name__ == "__main__":
    parser = init_cli_args()
    args = parser.parse_args()
    if args.no_template or args.template == '':
        args.template = None
    convert(args.markdown_file[0], args.base_url, args.template)
