###############################################################################
### To clean up your windows desktop, run this every monday at first log in ###
###############################################################################

import os
from datetime import date
from os import listdir

desktop = os.getenv('USERPROFILE') + '\\' + 'Desktop'
clean_dir = desktop + '\\' + 'clean_desktop'
last_week = date.today().isocalendar()[1]-1
last_week_dir = clean_dir + '\\' + str(last_week)
never_move = ['clean_desktop', 'desktop.ini', 'Trackjack41.lnk', 'Tools.lnk']  # Exclude these files and folders

if not os.path.exists(clean_dir):
    print('Creating "' + clean_dir + '" to store files in.')
    os.makedirs(clean_dir)

if not os.path.exists(last_week_dir):
    print('Creating folder for last week (Week: ' + str(last_week) + ').')
    os.makedirs(last_week_dir)

desktopfiles = listdir(desktop)  # Get all files and folders from desktop

# Tamper with the list to exclude things we don't want to move
for file in never_move:
    desktopfiles.remove(file)

# Move files
for file in desktopfiles:
    print('Moving "' + file + '"...')
    try:
        os.rename(desktop + '\\' + file, last_week_dir + '\\' + file)
    except WindowsError:
        print('Conflict detected...')
        conflicts_dir = last_week_dir + '\\' + '_conflicts'
        if not os.path.exists(conflicts_dir):
            os.makedirs(conflicts_dir)
        print('Moving "' + file + '" to "' + conflicts_dir + '".')
        os.rename(desktop + "\\" + file, conflicts_dir + '\\' + file)
print('All files and folders moved to "' + last_week_dir + '\\". Enjoy your clean desktop :)')