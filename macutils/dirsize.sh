#!/bin/bash

IFS=$(echo -en "\n\b")

for folder in `ls -1`
do
    du -skh "${folder}"
done
