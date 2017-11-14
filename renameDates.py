#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before date
    ((0|1)?\d)-                     # one or two digits for the month, possibly starting with 0 or 1
    ((0|1)?\d)-                     # one or two digits for the day, possibly starting with 0 or 1
    ((19|20)\d\d)                   # four digits for the year, first two must start with 19 or 20
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing. 
