#!/bin/bash
# Send POST request and print response body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
