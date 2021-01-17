PROJECT=pyexample
DIR=error test assets website

ifndef INSTALL_DIR
INSTALL_DIR=/usr/local/nginx
endif

install:
	test -d $(INSTALL_DIR)/$(PROJECT) || mkdir -p $(INSTALL_DIR)/$(PROJECT)
	install index.py $(INSTALL_DIR)/$(PROJECT)
	install __init__.py $(INSTALL_DIR)/$(PROJECT)
	install pyexample.conf $(INSTALL_DIR)/conf
	@for i in $(DIR);do cp -R $$i $(INSTALL_DIR)/$(PROJECT);done;