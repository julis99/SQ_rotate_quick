#!/bin/bash

directory="."  # Change this if you want to specify a different directory
prefix="000"
extension=".dnc"

dext_file_count=$(ls $directory/000*.dnc 2>/dev/null | wc -l)
new_number=$(printf "%06d" $((dext_file_count + 1)))
new_filename="$directory/$new_number$extension"

test_dancer_number=$((dext_file_count + 1))

options_b_g=("b/g" "b" "g")
options_0_1=("0" "1")

random_b_g=${options_b_g[$RANDOM % ${#options_b_g[@]}]}
random_0_1=${options_0_1[$RANDOM % ${#options_0_1[@]}]}
random_int=$((RANDOM % 11))

printf "TEST DANCER %d\n%s\n%s\n%s\n%s" "$test_dancer_number" "$new_number" "$random_b_g" "$random_0_1" "$random_int" > "$new_filename"
echo "Created file: $new_filename"