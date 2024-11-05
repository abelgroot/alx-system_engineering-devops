#!/usr/bin/env ruby
# Script to match a specific pattern using a regular expression
puts ARGV[0].scan(/hbt{2,5}n/).join
