#!/bin/bash

# check if directory argument is provided
if [ $# -eq 0 ]
then
  echo "Usage: $0 DIRECTORY"
  exit 1
fi

# check if directory exists
if [ ! -d "$1" ]
then
  echo "Error: $1 is not a directory"
  exit 1
fi

# find all png files in subdirectories of given directory
find "$1" -name "*.png" | while read file
do
  # run png_to_npy.py script
  python png_to_npy.py "$file"
done
