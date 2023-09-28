#!/bin/bash
# Makes a POST request for a JSON file
curl -sX POST -H "Content-type: application/json" -d @$2 $1
