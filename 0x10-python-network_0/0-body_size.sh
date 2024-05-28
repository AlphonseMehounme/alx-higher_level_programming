#!/bin/bash
# Print Request body size
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
