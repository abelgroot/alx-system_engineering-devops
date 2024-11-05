#!/usr/bin/env ruby
# Script to match and join only capital letters in a given string
puts ARGV[0].scan(/[A-Z]/).join
