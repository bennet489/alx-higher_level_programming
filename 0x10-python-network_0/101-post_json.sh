#!/bin/bash
# Send a Json and display the response
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
