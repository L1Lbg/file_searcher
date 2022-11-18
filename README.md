**Simple scanner that searchs for files in the PC where the script is executed** <br>
**Only** scans from home dir and below

**Usage**:
Run on your console :
```
python main.py file_you_are_searching_for
```
Or just execute the Python script and answer the input

Then, in the console a list will be printed which contains **all** of the files found in the PC

**If you want the script to be faster :** <br>
Enter the script, and edit in line 7, the variable to True, then it will only scan the principal directories that are in the list in line 19, this makes the scanning a lot faster. If you want to, change that list to your liking to target specific directories
