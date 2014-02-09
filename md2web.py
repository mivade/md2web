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
default_template_file = "template.html"

# File extensions that signify Markdown files.
_FILE_EXTENSIONS = ["md", "text", "markdown"]

# Markdown extensions to use.
md_extensions = ["extra", "codehilite", "latex"]

# Functions
# ---------

def convert(filename, template_filename=None, overwrite=False):
    """Compile the Markdown file filename into HTML."""
    output_filename = filename.split('.')[0] + '.html'
    if os.path.exists(output_filename) and not overwrite:
        print(output_filename, "exists and won't be overwritten.")
        return
    elif overwrite:
        print(output_filename, "exists. Overwriting.")
    else:
        print("Creating", output_filename)
    md = markdown.Markdown(extensions=md_extensions, output_format="xhtml1")
    with open(filename, 'r') as md_file:
        md_text = md_file.read()
        title = md_text.split('\n')[0].strip()
        html = md.convert(md_text)
    if template_filename:
        with open(template_filename, 'r') as template_file:
            template = template_file.read()
        template = re.sub("\$TITLE", title, template)
        template = re.sub("\$CONTENT", html, template)
        html = template
    with open(output_filename, 'w') as output_file:
        output_file.write(html)

def convert_directory(path, recurse=False, template_filename=None,
                      overwrite=False):
    """Convert all Markdown files in the given path."""
    # see https://mayankjohri.wordpress.com/2008/07/02/create-list-of-files-in-a-dir-tree/

# Main
# ----

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--overwrite", action="store_true",
                        help="Overwrite existing files.")
    parser.add_argument("--template", default=default_template_file,
                        help="HTML template file to use for conversion." + \
                        "Defaults to" + default_template_file)
    parser.add_argument("--no-template", action="store_true",
                        help="Don't use a template file.")
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Recurse through all directories and process " + \
                        "all Markdown files found.")
    parser.add_argument("markdown_file", nargs="?", default="__DIR__",
                        help="The Markdown file to read. If no file is " + \
                        "given, all Markdown files in the current " + \
                        "working directory (and subdirectories if -r is " + \
                        "given) will be processed.")
    args = vars(parser.parse_args())
    if args['no_template']:
        args['template'] = None
    convert(args['markdown_file'], args['template'], args['overwrite'])