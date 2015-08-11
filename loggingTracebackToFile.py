#! python3
# loggingTracebackToFile.py - shows how to log an error to a file to debug later

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

