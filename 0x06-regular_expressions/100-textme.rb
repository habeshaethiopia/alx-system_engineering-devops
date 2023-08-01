#!/usr/bin/env ruby

from = ARGV[0][/from:(\S+)\]/, 1]
to = ARGV[0][/to:(\S+)\]/, 1]
flag = ARGV[0][/flags:(\S+)\]/, 1]

puts "#{from},#{to},#{flag}"
