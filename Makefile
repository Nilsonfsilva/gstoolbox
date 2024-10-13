#!/usr/bin/env bash

# Project information
VERSION = 0.1.0
AUTHOR = Josenilson Ferreira da Silva
EMAIL = nilsonfsilva@hotmail.com
PACKAGE = gstoolbox

# Directories
PREFIX = /usr
INSTALL_DIR = $(PREFIX)/share/gstoolbox
DOC_DIR = $(PREFIX)/share/doc/gstoolbox
BIN_DIR = $(PREFIX)/bin

# Files
SRC_FILES = $(wildcard src/*)
DOC_FILES = doc/gstoolbox.1
SCRIPT = src/gstoolbox

# Native dependencies for Debian
DEBIAN_DEPENDENCIES = jq git curl nano original-awk bats

# Colors
GREEN := \033[1;32m
RED := \033[1;31m
BLUE := \033[1;34m
YELLOW := \033[1;33m
RESET := \033[0m

# Default target
all:
	@printf "gstoolbox $(VERSION) by $(AUTHOR) ($(EMAIL))\n"
	@printf "Use 'make install' to install or 'make uninstall' to remove.\n"

# Installation target
install: check_package_installed check_dependencies
	@printf "$(BLUE)Creating target directories if they don't exist...$(RESET)\n"
	mkdir -p $(INSTALL_DIR)
	@printf "$(BLUE)Copying the source files to $(YELLOW)$(INSTALL_DIR)$(RESET)...\n"
	cp $(SRC_FILES) $(INSTALL_DIR)
	@printf "$(BLUE)Copying the documentation to $(YELLOW)$(DOC_DIR)$(RESET)...\n"
	cp $(DOC_FILES) $(DOC_DIR)
	@printf "$(BLUE)Creating the symbolic link in $(YELLOW)$(BIN_DIR)$(RESET)...\n"
	ln -sf $(INSTALL_DIR)/gstoolbox $(BIN_DIR)/gstoolbox
	@printf "$(GREEN)Installation complete.$(RESET)\n"

# Uninstallation target
uninstall:
	@printf "$(RED)Removing installed files...$(RESET)\n"
	@printf "$(RED)$(YELLOW)$(INSTALL_DIR)$(RESET)\n"
	rm -rf $(INSTALL_DIR)
	@printf "$(RED)$(YELLOW)$(DOC_DIR)$(RESET)\n"
	rm -rf $(DOC_DIR)
	@printf "$(RED)$(YELLOW)$(BIN_DIR)/gstoolbox$(RESET)\n"
	rm -f $(BIN_DIR)/gstoolbox
	@printf "$(GREEN)Uninstallation complete.$(RESET)\n"

# Check if the package is already installed
check_package_installed:
	@if [ -d "$(INSTALL_DIR)" ]; then \
 		printf "$(YELLOW)Warning: $(PACKAGE) is already installed.$(RESET)\n" >&2; \
		false; \
	fi

# Check if Debian native dependencies are installed
check_dependencies:
	@printf "$(BLUE)Checking Debian native dependencies...$(RESET)\n"
	@for pkg in $(DEBIAN_DEPENDENCIES); do \
		if ! dpkg-query -W -f='${Status}' $$pkg 2>/dev/null | grep -q "install ok installed"; then \
			printf "$(RED)Installing $$pkg...$(RESET)\n"; \
			sudo apt-get install -y $$pkg; \
		else \
			printf "$(GREEN)$$pkg is already installed.$(RESET)\n"; \
		fi; \
	done

.PHONY: all install uninstall check_package_installed check_dependencies
