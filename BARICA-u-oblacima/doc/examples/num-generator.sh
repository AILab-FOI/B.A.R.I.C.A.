#!/usr/bin/env bash
# Random sequence generator
# Usage:
# num-generator.sh [num]
# where [num] is the number of
# random numbers to be generated
end=$1
for (( i=1; i<=end; i++ ))
do
    echo $RANDOM % 35 + 1 | bc
done
echo "\\x"
