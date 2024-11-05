#!/usr/bin/env ruby
# Script to match patterns like "hbn", "hbtn", "hbttn", "hbtttn", and "hbttttn" but not "hbon"
puts ARGV[0].scan(/hbt*n/).join
