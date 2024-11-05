#!/usr/bin/env ruby
# Script to match exactly a 10-digit phone number with no spaces or special characters
puts ARGV[0].scan(/^\d{10}$/).join
