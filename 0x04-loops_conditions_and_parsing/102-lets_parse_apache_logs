#!/bin/bash

# Path to the Apache log file
log_file="apache-access.log"

# Use awk to extract IP and HTTP status code
awk '{print $1, $9}' "$log_file"
