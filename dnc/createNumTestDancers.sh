#!/bin/bash

echo "Pls enter how many Dancers should be created:"
read count

if ! [[ "$count" =~ ^[0-9]+$ ]]; then
    echo "ERROR: Pls enter unsigned integer"
    exit 1
fi

for ((i=1; i<=count; i++)); do
    echo "Creating Test Dancer $i of $count"
    ./createNewTestDancer.sh
done

echo "Done! $count Test Dancers got created."