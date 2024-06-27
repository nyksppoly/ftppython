"""
Main Program    

Student ID: p2227436
Name: Ng Ye Kai
Class: DISM/FT/1B/01
Assesment: CA1-2

Script name: main.py

Purpose: to run the other scripts as needed

Usage syntax: click run button

Input file: ftpServerData

Output file: ftpClientData

Library/Module: 
    pip install python-nmap
    pip install prettytable

Known Issues:
    FTP Server runs into an error if there is already a prior instance running; exiting main.py does not shut down existing ftp server
"""
# Script start
import subprocess


# Menu start
x = 0
servercounter = False
while x != 4:
    x = input("**PSEC Info Security Apps**\n1) Scan Network\n2) Upload/Download file using FTP\n3) Send custom packet\n4) Quit\n>   ")
    try:
        x = int(x)
    except:
        print("Only Integers Allowed!")
    if x == 1:
        subprocess.call("nmap-scan.py", shell=True)
    elif x == 2:
        if servercounter == False:
            subprocess.Popen("ftp_server.py", shell=True)
            servercounter = True
        subprocess.call("ftp-client.py", shell=True)
    elif x == 3:
        subprocess.call("send-custom-packet.py", shell=True)
    elif x == 4:
        print("Exiting. Have a nice day!")
    else:
        print("Invalid Input!")