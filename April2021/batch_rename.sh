#!/bin/bash
for file in *.py
do
    mv "$file" "sol_$file"
done