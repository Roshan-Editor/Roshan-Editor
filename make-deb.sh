#!/bin/bash

# Configuration
_PACKAGE="roshan-editor"
_VERSION="1.0.0"
_ARCH="all"
REPO_URL="https://github.com/Roshan-Editor/Roshan-Editor.git"
PKG_NAME="${_PACKAGE}_${_VERSION}_${_ARCH}.deb"

echo "[+] Step 1: GitHub se Roshan-Editor download kar rahe hain..."
rm -rf Roshan-Editor
git clone "$REPO_URL"

if [ ! -d "Roshan-Editor" ]; then
  echo "[-] Error: Tool download nahi ho saka!"
  exit 1
fi

echo "[+] Step 2: Build Environment aur Files taiyar kar rahe hain..."
rm -rf build_env
mkdir -p build_env/DEBIAN
mkdir -p build_env/data/data/com.termux/files/usr/bin

# Files copy karein
cp -r Roshan-Editor/* build_env/data/data/com.termux/files/usr/bin/
chmod +x build_env/data/data/com.termux/files/usr/bin/* 2>/dev/null || true

# Control file
cat << CONTROL_EOF > build_env/DEBIAN/control
Package: $_PACKAGE
Version: $_VERSION
Architecture: $_ARCH
Maintainer: Roshan
Depends: bash, git, python
Section: utils
Priority: optional
Description: Custom Roshan Editor tool for Termux.
CONTROL_EOF

chmod 755 build_env/DEBIAN

echo "[+] Step 3: .deb Package bana rahe hain..."
dpkg-deb --build build_env "$PKG_NAME"
rm -rf build_env

echo "[+] Step 4: Termux Repo Index (Packages/InRelease) generate kar rahe hain..."

# Packages file banayein
apt-ftparchive packages . > Packages
gzip -c Packages > Packages.gz

# Release file banayein
cat << RELEASE_EOF > Release
Origin: Roshan Repository
Label: Roshan Tools
Suite: stable
Codename: termux
Architectures: all
Components: main
Description: Official Repository for Roshan Tools
RELEASE_EOF

apt-ftparchive release . >> Release

echo "--------------------------------------------------"
echo "[ SUCCESS ] Aapka .deb Package aur Repo taiyar hai!"
echo "--------------------------------------------------"

