#!/usr/bin/bash
# Request size
echo $(curl -w "%{size_download}" $1)
