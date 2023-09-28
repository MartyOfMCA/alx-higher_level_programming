#!/bin/bash
# Prints the response code for a request
curl -o /dev/null -sIw "%{http_code}" $1
