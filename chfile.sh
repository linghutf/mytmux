#!/bin/bash

if [[ $1 ]]; then
    for f in `find $1` ;do
        if [[ -f $f ]]; then
            chmod 644 $f
        elif [[ -d $f ]]; then
            chmod 755 $f
        fi
    done
fi

echo "done."
