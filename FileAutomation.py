#! python3
# FileAutomation.py - Quick automation of Malware Detection Feature

# import os module -- http://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/

# option 1 -- pull the files down from Kilo and sensor will see it

# option 2 -- replay pcap from endpoint 1 to endpoint 2 and sensor will see it

# ask for ip address of endpoint 1, and credentials

# ask for ip address of endpoint 2, assume its kilo.englab.sourcefire.com

# ask for ip address of DC, and credentials

# ask for ip address of Sensor and credentials

# have a copy of a file with all the malware filenames, another with clean files, another with neutral, another with unknown, another with preclass files in it, scp it to the endpoint

# ssh to endpoint 1, and run bash script, that calls all the filenames.
# example: cat /var/tmp/ | xargs wget http://kilo.englab.sourcefire.com

# ssh to DC, and use mysql to get database output, like filename, action, count, time, compare the values with the total number of files pulled down.

# print output saying to spotcheck DC WebUI for events and functionality of said feature.





