#!/bin/bash

# Bundle exercises.
current_dir=$(pwd)
while [ ! -d "$current_dir/.git" ]; do
    if [ "$current_dir" == "/" ]; then
        echo "Not in git repo. Ensure script is run from within git repo."
        exit 1
    fi

    current_dir=$(dirname "$current_dir")
done

cd "$current_dir/python/00_Introduction"

python3 -m pip install .