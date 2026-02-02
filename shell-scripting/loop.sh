#!/bin/bash
for i in {1..10}; do
[ $i -eq 5 ] && continue
[ $i -eq 8 ] && break
echo $i
done

#define function
function_name() {
    echo "This function calling happened."
}
# call function
function_name

count=1
while [ $count -le 5 ]; do
echo "Count: $count"
((count++))
done

