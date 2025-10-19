#!/bin/bash

# Check if correct number of arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: ./script.sh search_string replace_string folder"
    exit 1
fi

# Assign the arguments to variables for better readability
search_string=$1
replace_string=$2
folder=$3

# Find files containing the search string and replace it
grep -rl "$search_string" "$folder" | while read -r file
do
    # Replace the search string and list the file
    sed -i "s/$search_string/$replace_string/g" "$file"
    echo "Replaced in file: $file"
done

