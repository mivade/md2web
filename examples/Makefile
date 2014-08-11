CC = ../md2web.py --template ../templates/html5.html

all: $(shell find . -name "*.md" | sed 's/md/html/')

%.html: %.md
	$(CC) $<

clean:
	rm *.html
