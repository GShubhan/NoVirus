import sys
import os
   
#file handling -page 206

sys.stdout("Gabra - 12, MalwareScanner.")

#Directory to use, page 190- use of r insted of \\ in path
strDirPath = r'C:\download\'

fTimestamp = open("MStimestamp.txt", "r")
strTimestamp = fTimestamp.read()
strTimestamp =strTimestamp.rstrip('\n')

#https://pynative.com/python-list-files-in-a-directory/
#read directory listing and store in array
#search_dir = "/mydir/"
os.chdir(strDirPath)
arrayFiles = filter(os.path.isfile, os.listdir(strDirPath))
arrayFiles = [os.path.join(strDirPath, f) for f in arryFiles] # add path to each file
arrayFiles.sort(key=lambda x: os.path.getmtime(x))


#start loop for items in array 



# list to store files
res = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        res.append(file_path)
print(res)


#check the item , is it directory then ignore , we want to process only files


--------------------------------------
#extract datetime stamp from file,  https://python-forum.io/thread-32539.html
import os
from datetime import datetime
 
todays_date = datetime.now ()
today = todays_date.date ()
path = '/path/to/files/'
 
for filename in os.listdir (path) :
    file_time = os.path.getmtime (path + filename)
    file_date = datetime.fromtimestamp (file_time)
    file_day = file_date.date ()
    if file_day == today :
        print (f'File to copy is {path + filename}.')

----------------------------------
User this for listing and sorting files , path also gets added in this code . will be usefull fir MD5
import os

search_dir = "/mydir/"
os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))
---------------------------------
Use of idfile
            is_file = file.is_file() # <- possible PermissionError

        if not is_file:
            continue
