import os
from random import *
import sys
import time

#change this to your liking, if this condition is True, the program will run a lot faster
scan_only_principal_dirs = False
#-------------------------------

scanned_dirs = []
not_scanned_dirs = []
found_files = []
home_dir = os.path.expanduser('~')

if scan_only_principal_dirs == False:
	to_scan = [home_dir]
if scan_only_principal_dirs == True:
	#change if you want the principal dirs, adding them to the list
	to_scan = [home_dir + '/Desktop', home_dir + os.path.sep + 'Documents', home_dir + os.path.sep + '/Downloads', home_dir + os.path.sep + 'Dropbox', home_dir + os.path.sep + 'OneDrive',  home_dir + os.path.sep + 'Videos',  home_dir + os.path.sep + 'Photos']

#be able to execute the script with terminal arguments or just terminal
if len(sys.argv) == 1:
    term_searched = input('Input the file you are searching for : \n')

if len(sys.argv) == 2:
    term_searched = sys.argv[1]

#scan the directory inputed and adding directories to the to_scan list
def scan_dir(dir):
	scanned_dirs.append(dir)
	to_scan.remove(dir)
	try:
		os.chdir(dir)
		files = os.listdir()
		#looping through the dir
		for item in files:
			#if item is file just see if it matches with the query
			if os.path.isfile(item):
				if term_searched in item:
					found_files.append(str(os.getcwd()) + os.path.sep  + str(item))
		#if item is a dir and it has not been scanned, add it to the list to_scan
			if os.path.isdir(item):
				if item not in scanned_dirs:
					to_scan.append(str(os.getcwd()) + os.path.sep + str(item))
	except:
		not_scanned_dirs.append(dir)		

#do it until theres no dirs left to scan
while len(to_scan) != 0:
	scan_dir(to_scan[randint(0, len(to_scan) - 1)])

#output
print('Scanned ' + str(len(scanned_dirs)) + " directory(s) and couldn't scan " + str(len(not_scanned_dirs)) + " directory(s) because of permission problems")
if len(found_files) > 0:
	print('Found this file(s) with the requested name : \n' + str(found_files))
else:
	print("Couldn't find any file with that name")

time.sleep(5)
