PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin

install:
	install -d $(BINDIR)
	install -m 755 src/rainy.py $(BINDIR)/rainy
	chmod +x $(BINDIR)/rainy

uninstall:
	rm -f $(BINDIR)/rainy
