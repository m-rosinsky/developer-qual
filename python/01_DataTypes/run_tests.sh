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

# Navigate to workdir.
cd "$current_dir/python/01_DataTypes"

# Run tests.
python3 -m unittest tests.test
