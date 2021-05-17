#!/bin/bash


d1=`python3 -m site --user-site`

if ! [[ -e "$d1" ]]; then
  echo "Error.  Couldn't find d1".
  echo "  d1:  $d1"
  echo "  d1 was generated with the following command:"
  echo "    python3 -m site --user-site"
  echo "  Maybe you should try to create it manually and try to install again?"
  echo "  I'm not really sure."
  echo
  exit 1
fi

d2="$d1/prs"

if ! [[ -e "$d2" ]]; then
  mkdir "$d2"
fi


f="sandylib.py"
cp -f "$f" "$d2/$f"


cd "$d2"
if ! [[ -e "__init__.py" ]]; then
  touch "__init__.py"
fi




