#!/bin/bash
# Print Request body
if [ $(curl -s -w "%{http_code}" "$1")
