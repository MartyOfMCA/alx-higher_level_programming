#!/bin/bash
# Prints response body for a request
curl -siX OPTIONS $1 | grep "Allow: " | cut -d " " -f2-
