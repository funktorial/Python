#! python3
# renameDates.py - Renames community filenames

import shutil, os, re

# Create regex that matches files with the American date format.
titlePattern = re.compile(r"""^(.*?) # all text before episode number
    (S\d{,2}E\d{,2})                 # one or two digits for the month, possibly starting with 0 or 1
    (.*?)$                           # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory

for filename in os.listdir('F:\\Movies\\Community'):
    mo = titlePattern.search(filename)

    # Skip files without date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    epNumber   = mo.group(2)
    afterPart  = mo.group(3)

    # Form the new filename.
    #euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    newFilename = 'Community - ' + epNumber + '.mkv'

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('F:\\Movies\\Community')
    filename = os.path.join(absWorkingDir, filename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (filename, newFilename))
    shutil.move(filename, newFilename) # uncomment after testing. 
