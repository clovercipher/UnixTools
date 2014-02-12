#!/bin/bash

MD5A=`md5 $1 | cut -d ' ' -f 4`
MD5B=`md5 $2 | cut -d ' ' -f 4`


if [ $MD5A = $MD5B ]; then
	echo "Checksum matches"
else
	echo "These files do not match."
fi
