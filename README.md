md2web
======

Command line usage
------------------

`python md2web.py -h`

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
* `$TIMESTAMP` (optional): Adds a timestamp indicating the last time
  the file was modified. (Not yet implemented)
  
Bugs and Pitfalls
-----------------

* Right now, the first line of each source file *must* be the page
  title (the text that replaces `$TITLE`). In the future, this may
  change to something a little safer.
* Not overwriting files is not very intelligent at the moment. Without
  the `--overwrite` option, files will never be overwritten. In the
  future, it will check for recent modifications to the source file
  and automatically overwrite if necessary.
