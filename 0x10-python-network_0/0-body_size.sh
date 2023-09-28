#!/bin/bash
# Send a request to URL displaying the size of response body
curl -s $1 | wc -c
