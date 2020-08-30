#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
SongPattern = re.compile(r"""^(.*?) # all text before the date
    ((.+)\w)- # one or two digits for the month
    ((.+)\w) # one or two digits for the day
     # four digits for the year (must start with 19 or 20)
    ".mp3" # all text after the date
    """, re.VERBOSE)

def rename_util():
    # Loop over the files in the working directory.
    for amerFilename in os.listdir('.'):
        mp3 = SongPattern.search(amerFilename)
        # Skip files without suffix as ".mp3".
        if mp3 == None:
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
        shutil.move(amerFilename, euroFilename) # uncomment after testing                




import os
[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]




    

def main():
    loop = asyncio.get_event_loop()  # <12>
    result = loop.run_until_complete(supervisor())  # <13>
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
