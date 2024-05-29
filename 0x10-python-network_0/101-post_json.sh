#!/bin/bash
# POST request with content from file
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
