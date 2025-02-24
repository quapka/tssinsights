#!/usr/bin/env bash

if grep '#' "$1" > /dev/null; then
    cat "$1" \
        | tr --delete ' ' \
        | tr --delete '\n' \
        | tr '#' '\n'
else
    cat "$1"
fi
