import sys
import requests
import os
# Import hashlib library (md5 method is part of it)
import hashlib
import json
from matplotlib import pyplot as plt


sys.stdout.write("* Shubhan Gabra - 12, NoVirus Scanner *\n")
sys.stdout.write("=======================================\n \n")
api_key = "bcd5d9e1da8995675c233a23173504e4c434eed127eff2f6ecb0a5c897e753b2"



#Functions definition
def Getresult(hashes):
  headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"
    }
  params = {'apikey': api_key , 'resource':hashes}
  response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', params=params , headers=headers)
  json_response = response.json()

  return json_response

def printresult(hash):  
  getresult = Getresult(hash)
  print("last scanned: {}" .format(getresult.get('scan_date')))
  print("score:{}/{}".format(getresult.get('positives'),getresult.get('total')))
  return getresult

def GetTimestamp(StrTSfilename):
    #This fucntion will accept full path filename, read and return timestamp from that file
    #Returns epho value of 1st Jan 2023 if timestamp file does not exist
    if os.path.exists(StrTSfilename):
        sys.stdout.write('-Timestamp file exists! \n')
        flTimestamp = open(StrTSfilename, "r")
        strlTimestamp = flTimestamp.read()
        strlTimestamp =strlTimestamp.rstrip('\n')
        flTimestamp.close()
        flotlTimestamp=float(strlTimestamp)
        print(StrTSfilename)
    else:
        sys.stdout.write('-The file does not exist \n-Using 1st Jan 2023 \n')
        flotlTimestamp =float('1672531200')
        #set epoch of 1st Jan 2023 
    return flotlTimestamp

#Directory to use, program will look into this folder
strDirPath = r'C:\Users\shubhan\Downloads'
strProgramPath = r'C:\Users\Shubhan\Desktop\NoVirus'

#Read timestamp file 
sys.stdout.write('Reading timestamp file \n')
flotTimestamp =float('0')
strTimestampFile = strProgramPath + r"\MStimestamp.txt"
flotTimestamp = float(GetTimestamp(strTimestampFile))
sys.stdout.write('Value of timestamp:' + str(flotTimestamp) + '\n \n')

os.chdir(r'C:\Users\shubhan\Downloads')
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
    TargetFile = strDirPath +"\\" + strFile
    sys.stdout.write('-Processing file: ' + TargetFile + '\n')
    file_time = os.path.getmtime (TargetFile)
    sys.stdout.write('-File timestamp: '+ str(file_time) + '\n')
    if file_time > flotTimestamp:
        sys.stdout.write('-This is new file, generating MD5 \n')
        intNewFileFound = 1
        #Generate MD5 of this file
        strTargetfile = open(TargetFile, 'rb')
        # read binary data of the file
        bnrData = strTargetfile.read()
        # pipe contents of the file through
        strMD5 = hashlib.md5(bnrData).hexdigest()
        strTargetfile.close()
        sys.stdout.write('-MD5 for file : ' + strMD5 + '\n')
        sys.stdout.write('-Checking virustotal raputation \n')
        FileResults=printresult(strMD5)
        pos=FileResults.get('positives')
        tot=FileResults.get('total')
        if pos!= None:
            colors=['red','green']
            Result=['Malicious', 'Non-malicious']
            Score=[int(pos),int(tot)-int(pos)]
            plt.pie(Score, labels=Result, autopct='%1.0f%%',colors=colors)
            plt.title("Antivirus scan:  \n"+TargetFile)
            plt.show()
            

    #Do we have new file created after last run?
sys.stdout.write('End of file processing \n')

if intNewFileFound == 1:
    sys.stdout.write('\nUpdating timestamp file with new timesstamp \n')
    fTimestamp = open(strTimestampFile, "w")
    fTimestamp.write(str(file_time))
    fTimestamp.close()
else:
    sys.stdout.write('No new file found \n \n')

    

print('\n *****End of Program******')

