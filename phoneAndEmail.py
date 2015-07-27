#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on th clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)?                          # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5})))?     # extention
    )''', re.VERBOSE)

# TODO: Create email regix.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard
