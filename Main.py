import sys
import os
# Import hashlib library (md5 method is part of it)
import hashlib

#import win32api  easy_install PyWin32
#import tkinter
#from tkinter import messagebox

#root = tkinter.Tk()
#root.withdraw()
# Message Box
#messagebox.showinfo("Title", "Message")

#win32api.MessageBox(0, 'hello', 'title')

sys.stdout.write("* Shubhan Gabra - 12, NoVirus Scanner *\n")
sys.stdout.write("=======================================\n \n")

#Functions definition
def GetTimestamp(StrTSfilename):
    #This fucntion will accept full path filename, read and return timestamp from that file
    #Returns epho value of 1st Jan 2023 if timestamp file does not exist
    if os.path.exists(StrTSfilename):
        sys.stdout.write('-Timestamp file exists! \n')
        flTimestamp = open(StrTSfilename, "r")
        strlTimestamp = flTimestamp.read()
        strlTimestamp =strTimestamp.rstrip('\n')
        flTimestamp.close()
        flotlTimestamp=float(strlTimestamp)
    else:
        sys.stdout.write('-The file does not exist \n-Using 1st Jan 2023 \n')
        flotlTimestamp =float('1672531200')   #set epoch of 1st Jan 2023 
    return flotlTimestamp

#Directory to use, program will look into this folder
strDirPath = '.'
strProgramPath = '.'

#Read timestamp file 
sys.stdout.write('Reading timestamp file \n')
flotTimestamp =float('0')
strTimestampFile = strProgramPath + "/MStimestamp.txt"
flotTimestamp = float(GetTimestamp(strTimestampFile))
sys.stdout.write('Value of timestamp:' + str(flotTimestamp) + '\n \n')


Strfilename=os.getcwd()
sys.stdout.write('Current directory is '+ Strfilename + '\n')

# Iterate directory
# list to store files
sys.stdout.write('Reading directory listing \n \n')
res = []
intNewFileFound = 0
for Strfilename in os.listdir(strDirPath):
    # check if current item is file or folder, we will check only files and ignore folders
    if os.path.isfile(os.path.join(strDirPath, Strfilename)):
        		res.append(Strfilename)
#Now we have all new files created after last run in arrary res

sys.stdout.write('Processing new files found \n')
for strFile in res:
    #check if file is new created after last run
    sys.stdout.write('-Processing file: ' + strFile + '\n')
    file_time = os.path.getmtime (strDirPath + '/' + strFile)
    sys.stdout.write('-File timestamp: '+ str(file_time) + '\n')
    if file_time > flotTimestamp:
        sys.stdout.write('-This is new file, generating MD5 \n')
        intNewFileFound = 1
        #Generate MD5 of this file
        strTargetfile = open(strDirPath + '/' + strFile, 'rb')
        # read binnary data of the file
        bnrData = strTargetfile.read()
        # pipe contents of the file through
        strMD5 = hashlib.md5(bnrData).hexdigest()
        strTargetfile.close()
        sys.stdout.write('-MD5 for file : ' + strMD5 + '\n')
        sys.stdout.write('-Checking virustotal raputation \n')
    #Do we have new file created after last run?
sys.stdout.write('End of file processing \n')

if intNewFileFound == 1:
    sys.stdout.write('\nUpdating timestamp file with new timesstamp \n')
    fTimestamp = open("MStimestamp.txt", "w")
    fTimestamp.write(str(file_time))
    fTimestamp.close()
else:
    sys.stdout.write('No new file found \n \n')

print('\n *****End of Program******')
