#! python3
# oswalk.py - Goes over the current directory and sub directories and folders and prints out the contents
# Usage: python3 oswalk.py

import os
for folderName, subfolders, filenames in os.walk('/Users/mnobile'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

