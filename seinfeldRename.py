#! python3
# seinfeldRename.py - Renames Seinfeld filenames

import shutil, os, re

# Create regex that matches files with the American date format.
titlePattern = re.compile(r"""^(.*?) # all text before episode number
    (S\d{,2}E\d{,2})                 # one or two digits for the month, possibly starting with 0 or 1
    (\D*)                            # Nonnumerical test after episode number
    (.*?)$                           # all text after 
    """, re.VERBOSE)

# Loop over the files in the working directory

for filename in os.listdir('F:\\Movies\\Seinfeld'):
    mo = titlePattern.search(filename)

    # Skip files without date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    epNumber   = mo.group(2)
    epTitle    = mo.group(3)
    afterPart  = mo.group(4)

    # Fix Title
    newEpTitle = epTitle.replace('.', ' ') #replaces periods with spaces
    if newEpTitle.startswith(' ') and newEpTitle.endswith(' '):
        newEpTitle = newEpTitle[1:-1] #strips extreme spaces

    # Form the new filename.
    newFilename = 'Seinfeld ' + epNumber + ' - ' + newEpTitle + '.mkv'

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('F:\\Movies\\Seinfeld')
    filename = os.path.join(absWorkingDir, filename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (filename, newFilename))
    shutil.move(filename, newFilename) # uncomment after testing. 
