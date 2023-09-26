# Define installation paths
PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin

install:
	install -D -m 755 src/rainy.py $(BINDIR)/rainy
	chmod +x $(BINDIR)/rainy

uninstall:
	rm -f $(BINDIR)/rainy
