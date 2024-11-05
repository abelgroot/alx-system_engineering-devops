#!/usr/bin/env ruby
# Script to match patterns like "hbtn", "hbttn", "hbtttn", and "hbttttn"
puts ARGV[0].scan(/hbt{1,4}n/).join
