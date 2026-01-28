#!/bin/bash 
# This is a single line comment
: '
This is a multi-line comment
which spans multiple lines.
'
set -e  # Exit immediately if a command exits with a non-zero status (exist on error)


name="Jaswanth"  #variable assignment (no spaces around =)
echo "Hello, $name!"

current_date=$(date)  #command substitution
echo "Current date and time: $current_date"

