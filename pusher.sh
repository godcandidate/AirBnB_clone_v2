#!/bin/bash

echo "Enter filename"
read filename

git add $filename
git commit -m "update $filename"
git push
