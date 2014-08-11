md2web
======

Command line usage
------------------

```
usage: md2web.py [-h] [--template TEMPLATE] [--no-template] markdown_file

positional arguments:
  markdown_file        The Markdown file to convert to HTML.
  
  optional arguments:
    -h, --help           show this help message and exit
	--template TEMPLATE  HTML template file to use for conversion. Defaults to
                         template.html
	--no-template        Don't use a template file.						 
```

Requirements
------------

* [Python Markdown][]
* [Jinja2][]

[Python Markdown]: http://pythonhosted.org/Markdown/index.html
[Jinja2]: http://jinja.pocoo.org/

Templates
---------

`md2web` can use templates to keep things looking consistent
throughout an entire site. To create a template from scratch, just
include whatever you want and make sure to use the following variables
somewhere in the document:

* `$CONTENT`: This is where all the Markdown-compiled text will be
  placed.
* `$TITLE`: The document title to place between `<title>` and
  `</title>`.
  
Bugs and Pitfalls
-----------------

* Right now, the first line of each source file *must* be the page
  title (the text that replaces `$TITLE`). In the future, this may
  change to something a little safer.
* Rather than build in code to determine whether or not a file needs
  to be rebuilt, something like `make` should be used instead. See the
  example makefile in the `examples` directory.
  
TODO
----

[ ] Update usage information to reflect using Jinja2.

[ ] Add support for more output formats (via command-line arguments).
  
License
-------

`md2web` is released under the terms of the GNU GPL version 3.
