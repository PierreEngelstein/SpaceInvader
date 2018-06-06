INSTALL_DIR=/usr/local/bin/SpaceInvader
SRC_DIR=src
BIN_DIR=bin

edit:
	mkdir -p $(BIN_DIR)
	python -m compileall $(SRC_DIR)/*.py
	cp $(SRC_DIR)/*.pyc $(BIN)/
	rm -rf $(SRC_DIR)/*.pyc
	cp -r $(SRC_DIR)/resources $(BIN_DIR)/resources

install:
	mkdir -p $(INSTALL_DIR)
	cp -a $(BIN_DIR)/ $(INSTALL_DIR)

uninstall:
	rm -rf $(INSTALL_DIR)

push:
	echo "PUSHINNG PUSHIIING"

clean:
	rm -rf $(SRC_DIR)/*.pyc
	rm -rf $(BIN_DIR)/
