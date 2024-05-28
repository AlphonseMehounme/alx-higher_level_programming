#!/bin/bash
# Print Request body size
echo $(curl -s -o "%{stdout}" "$1")
