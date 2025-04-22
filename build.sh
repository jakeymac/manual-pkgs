#!/bin/bash

# Text colors
GREEN_TEXT='\033[0;32m'
RESET_COLOR='\033[0m'

set -e

PKG_NAME="manual-pkgs"
VERSION="1.0.1"
BUILD_ROOT="dist/${PKG_NAME}_${VERSION}"
BIN_PATH="$BUILD_ROOT/usr/bin"

echo "Cleaning up old build..."
rm -rf "$BUILD_ROOT" "dist/${PKG_NAME}_${VERSION}.deb"
mkdir -p "$BUILD_ROOT/DEBIAN"
mkdir -p $BIN_PATH

echo "Staging files..."
cp control "$BUILD_ROOT/DEBIAN/control"
cp get_manual_pkgs.py "$BIN_PATH/manual-pkgs"
chmod +x "$BIN_PATH/manual-pkgs"

echo "Building .deb..."
dpkg-deb --build "$BUILD_ROOT"

echo -e "${GREEN_TEXT}Done building dist/${PKG_NAME}_${VERSION}.deb${RESET_COLOR}"
