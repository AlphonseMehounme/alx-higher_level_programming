#!/bin/bash
# Print Request body size
touch bodyfile
code=$(curl -s -o bodyfile -w "%{http_code}" "$1")
if [ $code -eq 200 ]; then
	cat bodyfile
fi
