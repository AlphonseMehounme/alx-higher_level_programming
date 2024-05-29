#!/bin/bash
# Print server Allow methods
curl -s --request-target "*" -X OPTIONS "$1"
