#!/bin/bash


directory="."  # Change this if you want to specify a different directory
prefix="000"

find "$directory" -type f -name "${prefix}*.dnc" -exec rm -f {} +

echo "All .dnc files starting with $prefix have been removed."