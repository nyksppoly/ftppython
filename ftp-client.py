# Ref: https://pythonspot.com/ftp-client-in-python/

import ftplib, os
ftp = ftplib.FTP()
ftp.connect('localhost', 2121)
ftp.login()
os.chdir("ftpClientData/")
# list files in server directory
print("All files in server directory: ")
ftp.retrlines('LIST')

# Download file from ftpServerData
def getFile(ftp, filename):
  try:
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    return(True)
  except:
    return(False)

# Upload file from ftpClientData
def upFile(ftp, filename):
  file = open(filename,"rb")                      # file to send
  ftp.storbinary("STOR "+ filename, file)         # send the file
  file.close()                                    # close file and FTP

# Menu start
x = 0
while x != 3:
  x = input("1) Upload a file\n2) Download a file\n3) Quit\n>  ")
  try:
    x = int(x)
  except:
    print("Only Integers Allowed!")
  if x == 1:
    uploadname = input("Filename to be uploaded: ")
    upFile(ftp, uploadname)
  elif x == 2:
    file_download = input("filename to be downloaded: ") # you should specify your own file
    if (getFile(ftp,file_download)):
      print(f'Downloaded file: {file_download}')
    else:
      print(f'Error in downloading: {file_download}')
  elif x == 3:
    print("Thank you and goodbye!")
  else:
    print("Invalid Input!")
ftp.quit()
