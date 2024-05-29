#!/bin/bash
# Print server Allow methods
curl -s -I -X OPTIONS "$1" | grep "Allow" | sed "s/Allow: //"
