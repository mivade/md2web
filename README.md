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
  
<!--
TODO:
* `$TIMESTAMP` (optional): Adds a timestamp indicating the last time
  the file was modified.
-->
  
Bugs and Pitfalls
-----------------

* Right now, the first line of each source file *must* be the page
  title (the text that replaces `$TITLE`). In the future, this may
  change to something a little safer.
* I decided to have `make` handle things like determining whether or
  not an HTML file needs updating. See the example makefile in the
  `examples` directory.
  
License
-------

`md2web` is released under the terms of the GNU GPL version 3. This
does not include the `mdx_latex.py` file
[originally authored][mdx_latex] by Justin Bruce Van Horne and
released under the [Creative Commons Public Domain Mark 1.0][CCPDL1]
license.

[mdx_latex]: https://github.com/justinvh/Markdown-LaTeX
[CCPDL1]: http://creativecommons.org/publicdomain/mark/1.0/
