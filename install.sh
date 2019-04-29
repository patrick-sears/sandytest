#!/bin/bash


progdir=`pwd -P`
name="sandytest"

if [[ -e "$HOME/bin" ]]; then
  cd "$HOME/bin"
  if [[ -L "$name" ]]; then
    unlink "$name"
  fi
  ln -s "$progdir/main.py" "$name"
else
  echo "No home bin dir, so not creating any link."
fi



cd "$progdir/libs"
./install_lib.sh




