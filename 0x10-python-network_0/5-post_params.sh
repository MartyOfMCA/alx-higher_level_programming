#!/bin/bash
# Sends a POST request with data added to teh request body
curl -sd email=test@gmail.com -d subject="I will always be here for PLD" $1
