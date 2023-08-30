4 design requirements 
Files :
I have used one file to store timestamp of last file scanned. The program will read timestamp file at the start and process downloaded files after that Date-Time. This file will be rewritten at the end of the program with new timestamp to be used in next run.

Functions :
Sys
	Sys.stdout
OS
	Os.listdir
	Os.chdir
	Os.path.isfile
_main
If -elif
File


System requirements
NoVirus scanner will require following minimum system requirements. 
Windows 8/10/11
Processor:1 GHz or faster.
Minimum RAM:1 GB (32-bit) or 2 GB (64-bit)
Hard disk space:16 GB (32-bit) or 20 GB (64-bit)
Display:800×600 resolution.




 

Algorithm and flow chart

Flowchart


Algorithm

Step 1 : Set the watch folder - We will set "Download Folder"
Step 2 : Read DtLastDateTimeStamp from file 'LastScan.txt'
Step 3 : Extract File list, sorted with time Desc from the watch folder 
Step 4 : Iterate through the file listing - store File name in StrCurrentFileName and Date Timestamp of file in DTDateTime variable
 Step 5 :  If DTDateTime > DtLastDateTimeStamp     'We have a new file in download folder
      Step 5.1 : Generate FileHash and store strFileHash for file StrCurrentFileName
      Step 5.2 : Call Virus total API to search strFileHash and store Score in the iHashScore
     Step 5.3:  If iHashScore > 5 
        		Step 5.3.1 : 'likely Malicious file, Create pop up alert " Malware Scanner has detected a mailious file StrCurrentFileName in watch folder
 Step 6:  End loop - all files searched 
Step 7: update file 'LastScan.txt' with new DateStamp DTDateTime


Code listing
import sys
import os
# Import hashlib library (md5 method is part of it)
import hashlib

sys.stdout("Shubhan Gabra - 12, NoVirus Scanner.")

#Directory to use, program will look into this folder
strDirPath = r'C:\download\'
#Read timestamp file 
fTimestamp = open("MStimestamp.txt", "r")
strTimestamp = fTimestamp.read()
strTimestamp =strTimestamp.rstrip('\n')

#read directory listing and store in array
# list to store files
res = []

# Iterate directory
for Strfilename in os.listdir(strDirPath):
    # check if current item is file or folder, we will check only files and ignore folders
    if os.path.isfile(os.path.join(strDirPath, Strfilename)):
        		res.append(Strfilename)
print(res)
#Now we have all new files created after last run in arrary res

#Read arrary and process each file
for strFile in res:

       	#check if file is new created after last run 
	file_time = os.path.getmtime (strDirPath + Strfilename)
   	file_date = datetime.fromtimestamp (file_time)
    	file_day = file_date.date ()
    	if file_day == strTimestamp:    # today :   change here to >= , debug 
        		print (f'File to add in list is { strDirPath + Strfilename }.')
 	
	# read file and calculate MD5 of file 
	with open(strFile, 'rb') as strCheckfile:
	# read contents of the file
	bnrData = strCheckfile()    
	# pipe contents of the file through
	strMD5 = hashlib.md5(bnrData).hexdigest()
	print(strMD5)

	#call VirusTotal API 
	
	#Check reputation 
	
	#alert 
	
	#update strTimestamp

user documentation
	Input/Output run screen

Bibliography 
