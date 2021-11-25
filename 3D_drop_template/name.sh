#!/bin/bash

dirname="${PWD##*/}"
myarr=($(echo $dirname | tr "_" "\n"))

for i in "${myarr[@]}"
do
	echo $i
done
