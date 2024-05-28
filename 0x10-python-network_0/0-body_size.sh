#!/bin/bash
# Print Request body size
echo $(curl -w "%{size_download}" $1)
