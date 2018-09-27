#!/usr/bin/env python

import os, sys

def time_to_seconds(hour, minute, second):
    return 60*60*int(hour) + 60*int(minute) + int(second)

def getPeriod(time_instance):
    [hour, minute, second] = time_instance.split(":")

    instance_seconds = time_to_seconds(hour, minute, second)
    if(instance_seconds >= time_to_seconds("06","50","00") and
       instance_seconds <= time_to_seconds("09","10","00")):
        return "[1]breakfast"
    elif(instance_seconds >= time_to_seconds("10","20","00") and
         instance_seconds <= time_to_seconds("14","30","00")):
        return "[2]lunch"
    elif(instance_seconds >= time_to_seconds("17","20","00") and
         instance_seconds <= time_to_seconds("19","50","00")):
        return "[3]dinner"
    else:
        return "[------]unknown"


if(len(sys.argv) < 2):
    print 'ERROR: Too few arguments. Please enter the path of the file to be filtered'
else:
    with open(sys.argv[1]) as datafile:
        if(not os.path.exists("FILTERED")):
            os.makedirs("FILTERED")

        lastFilePath = ""
        file = open("FILTERED/Header.txt", "w")
        file.write("Catraca filter. All months are separated in directories, files are determined by day and by time period (1_breakfest, 2_lunch, 3_dinner)")

        for line in datafile:
            [date, time_instance] = line.split(' ')
            [year,month,day] = date.split('-')

            period = getPeriod(time_instance)

            dirname = "FILTERED/" + year + "/" + month;
            if(not os.path.exists(dirname)):
                os.makedirs(dirname)

            newFilePath = "FILTERED/" + year + "/" + month + "/day(" + day + ")_" + period
            if(newFilePath != lastFilePath):
                file.close()
                file = open(newFilePath, "w")
            lastFilePath = newFilePath

            file.write(time_instance)
            # if(day != lastDay):
            #     print "day", date
            # lastDay = day

