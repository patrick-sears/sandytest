#!/bin/bash


d1=`python3 -m site --user-site`

if ! [[ -e "$d1" ]]; then
  echo "Error.  Couldn't find d1".
  echo; exit 1
fi

d2="$s1/prs"

if ! [[ -e "$d2" ]]; then
  mkdir "$d2"
fi


f="sandylib.py"
cp -f "$f" "$d2/$f"




