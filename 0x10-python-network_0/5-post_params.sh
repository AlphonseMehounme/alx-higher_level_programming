#!/bin/bash
# Send POST request and print response body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1" # -X POST "$1"
