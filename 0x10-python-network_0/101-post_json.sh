#!/bin/bash
# POST request with content from file
curl -s -d @"$2" -X POST "$1"
