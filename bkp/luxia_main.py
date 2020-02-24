from sftp import *

myHostName = "52.47.123.17"
myUsername = "ibbl"
keyFile = "M:\IBBL BIS\Certificates\LUXIA\Luxia-sftp"
local = "P:\LUXIA\Folder"

print("is extension correct", check_extension(local))
print("is files contain the correct R1 and R2", check_number_file_r1_r2(local))

if check_file(local):
    print("le fichier est bon")
else:
    print("le fichier est KO")

connect_to_sftp(myHostName, myUsername, keyFile)
