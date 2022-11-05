import os
from random import *
import sys

scanned_dirs = []
found_files = []
home_dir = os.path.expanduser('~')
to_scan = [home_dir]

#be able to execute the script with terminal arguments or just terminal
if len(sys.argv) == 1:
         term_searched = input('Input the file you are searching for : \n')

if len(sys.argv) == 2:
        term_searched = sys.argv[1]

#scan the directory inputed and adding directories to the to_scan list
def scan_dir(dir):
	scanned_dirs.append(dir)
	to_scan.remove(dir)
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

#do it until theres no dirs left to scan
while len(to_scan) != 0:
	scan_dir(to_scan[randint(0, len(to_scan) - 1)])

#output
print('Scanned ' + str(len(scanned_dirs)) + ' directory(s)')
print('Found this files ' + str(found_files))
