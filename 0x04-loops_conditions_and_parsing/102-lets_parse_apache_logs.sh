#!/bin/bash

# Path to the Apache log file
log_file="apache-access.log"

# Use awk to extract IP and HTTP status code, then group and sort
awk '{print $1, $9}' "$log_file" | sort | uniq -c | sort -nr | awk '{print $1, $2, $3}'
