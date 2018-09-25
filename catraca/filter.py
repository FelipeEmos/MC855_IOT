#!/usr/bin/env python

import os, sys

if(len(sys.argv) < 2):
    print 'ERROR: Too few arguments. Please enter the path of the file to be filtered'
else:
    with open(sys.argv[1]) as datafile:

        lastDay = ""

        for line in datafile:
            elements = line.split(' ')
            day = elements[0]
            if(day != lastDay):
                print "Day ", day
            lastDay = day

