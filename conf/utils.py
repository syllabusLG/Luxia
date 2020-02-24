import email, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# FTP Variables
myHostName = "52.47.123.17"
myUsername = "ibbl"
keyFile = "/home/robot/bin/LUXIA/sftp-key/Luxia-sftp"
KeyFileWrong = ""

# email Variables
host = "smtp.lih.lu"
port = "25"
fromaddr = "IBBL - LUXIA FastQ File transfer <robot@lih.lu>"

# Folders
path = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/ROUTINE/"
pathMove = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/BKP/"
#path = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/BKP/"
files = os.listdir(path)
var_files = []
check_sum_file = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/ROUTINE/luxia_list.md5"
#check_sum_file = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/BKP/luxia_list.md5"

# Distribution Lists
client=['contact@luxia-scientific.com']
#client=['abousyllaba.ndiaye@devoteam.lu']
bioref = ['lorieza.castillo@ibbl.lu', 'wim.ammerlaan@ibbl.lu']
#bioref = ['Fabien.Perry@ibbl.lu', 'David.Kern@ibbl.lu']
pm = ['maria-manuela.tonini@ibbl.lu']
#pm = ['syllaba89@gmail.com']
bis = ['abousyllaba.ndiaye@ibbl.lu','ariane.assele-kama@ibbl.lu']
bis_pm =pm + bis
ibbl = pm + bioref + bis 
helpdesk = ['helpdesk@lih.lu']

# For Testing purposes
#path = "/labdata/Hierarchy/METADATA_ROUTINE/_LUXIA_DATA_TRANSFER/DONT_TOUCH_FOR_TESTS_PURPOSES/"
#cas1 = path + "CASE1-NOT-ONLY-LX/"
#cas2 = path + "CASE2-OK/"
#cas3 = path + "CASE3-IMPAIR/"
#cas4 = path + "CASE4-EXTENSION/"
#cas5 = path + "CASE5-NOT-A-FOLDER"
#cas6 = path + "CASE6-FOLDER-EMPTY/"

if os.path.isdir(path):
    files = os.listdir(path)
    for file in files:
        var_files.append(file+"\r\n")
        
list_files = ''.join(var_files)
        
#check_sum_file = path + "luxia_list.md5"
#client = 'ariane.asselekama@gmail.com'
#bioref = ['ariane.assele-kama@ibbl.lu', ';abousyllaba.ndiaye@ibbl.lu']
#pm = ['ariane.assele-kama@ibbl.lu', ';syllaba89@gmail.com', ';ariane.asselekama@gmail.com']
#bis = ['ariane.assele-kama@ibbl.lu', ';abousyllaba.ndiaye@ibbl.lu', ';ariane.asselekama@gmail.com']
#ibbl = pm + [';'] + bioref + [';'] + bis + [';'] + ['ariane.assele-kama@ibbl.lu']
#helpdesk = 'ariane.assele-kama@ibbl.lu'

# Folder doesn't exist
folder_msg = MIMEMultipart()
#folder_msg['From'] = fromaddr
#folder_msg['To'] = ''.join(helpdesk)
#folder_msg['Cc'] = ''.join(bis)
#folder_msg['Subject'] = "[ERROR] LUXIA - FastQ transfer files - Folder doesn't exist"
start = """Dear IT Team,\r\n \r\n Please have a look on the folder located at \r\n \r\n"""
end = """\r\n \r\n It seems that this path doesn't not exist anymore. Please have a look in order to perform the Luxia transfer.\r\n \r\n No files have been sent to the client.\r\n \r\n Regards.\r\n IT Business Information Solution"""
body = start + format(path) + end
folder_msg.attach(MIMEText(body, 'html'))
folder_msg_subject = "[ERROR] LUXIA - FastQ transfer files - Folder doesn't exist"
folder_msg = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ' '.join(helpdesk)+ "CC: %s\r\n" % ','.join(bis)+ "Subject: %s\r\n" % folder_msg_subject+ "\r\n"+ body
toHelpdesk =helpdesk + bis
#message_to_bis = folder_msg.as_string()

# Cannot access to FTP
ftp_msg = MIMEMultipart()
#ftp_msg['From'] = fromaddr
#ftp_msg['To'] = client
#ftp_msg['Cc'] = ''.join(ibbl)
#ftp_msg['Subject'] = "[ERROR] LUXIA - FastQ transfer files - Cannot access to the FTP"
body = """Dear CLient,\r\n \r\n We are facing some errors to access to your FTP site.\r\n \r\n Could you please have a look and come back to us ?.\r\n \r\n Regards.\r\n IT Business Information Solution"""
ftp_msg.attach(MIMEText(body, 'html'))
ftp_msg_subject =  "[ERROR] LUXIA - FastQ transfer files - Cannot access to the FTP"
ftp_msg = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ' '.join(client)+ "CC: %s\r\n" % ','.join(ibbl)+ "Subject: %s\r\n" % ftp_msg_subject+ "\r\n"+ body
toFtp =client + ibbl
#message_for_ftp_error = ftp_msg.as_string()

# Incorrect Luxia files
biorep_msg = MIMEMultipart()
#biorep_msg['From'] = fromaddr
#biorep_msg['To'] = ''.join(bioref)
#biorep_msg['Cc'] = ''.join(bis) + ";" + ''.join(pm)
#biorep_msg['Subject'] = "[ERROR] LUXIA - FastQ transfer files - Incorrect Luxia files in the folder (number and/or extension)"
start = """Dear BIOREF Team,\r\n \r\n Please have a look on the files list below : \r\n \r\n"""
end = """\r\n \r\n There is an error on the list provided for FTP transfer to LUXIA. Please have a look on the number of files and/or extension, and correct them in order to perform the Luxia transfer.\r\n \r\n No files have been sent to the client.\r\n \r\n Regards.\r\n IT Business Information Solution"""
body = start + list_files + end
biorep_msg.attach(MIMEText(body, 'html'))
biorep_msg_subject = "[ERROR] LUXIA - FastQ transfer files - Incorrect Luxia files in the folder (number and/or extension)"
biorep_msg = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ','.join(bioref)+ "CC: %s\r\n" % ','.join(bis_pm)+ "Subject: %s\r\n" % biorep_msg_subject+ "\r\n"+ body
toBio =bioref +  bis_pm
#message_error_bad_luxia = biorep_msg.as_string()

# Incorrect not only Luxia files
biorep_msg2 = MIMEMultipart()
#biorep_msg2['From'] = fromaddr
#biorep_msg2['To'] = ''.join(bioref)
#biorep_msg2['Cc'] = ''.join(bis) + ";" + ''.join(pm)
#biorep_msg2['Subject'] = "[ERROR] LUXIA - FastQ transfer files - Incorrect Luxia files in the folder (wrong extension)"
start = """Dear BIOREF Team,\r\n \r\n Please have a look on the files list below : \r\n \r\n """
end = """\r\n \r\n There is an error on the  list provided for FTP transfer to LUXIA. Some files are not respecting Luxia files naming rules. Please have a look and correct them in order to perform the Luxia transfer.\r\n \r\n No files have been sent to the client.\r\n \r\n Regards.\r\n IT Business Information Solution"""
body = start + list_files + end
biorep_msg2.attach(MIMEText(body, 'html'))
biorep_msg2_subject = "[ERROR] LUXIA - FastQ transfer files - Incorrect Luxia files in the folder (wrong extension)"
biorep_msg2 = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ','.join(bioref)+ "CC: %s\r\n" % ','.join(bis_pm)+ "Subject: %s\r\n" % biorep_msg2_subject+ "\r\n"+ body
toBio2 =bioref + bis_pm
#message_error_not_only_luxia = biorep_msg2.as_string()

# Success
client_msg = MIMEMultipart()
#client_msg['From'] = fromaddr
#client_msg['To'] = ''.join(client)
#client_msg['Cc'] = ''.join(ibbl)
#client_msg['Subject'] = "[SUCCESS] LUXIA - FastQ transfer files"
start = """Dear Client,\r\n \r\n Please find below the FastQ files transfered.\r\n \r\n"""
end = """\r\n \r\n Regards.\r\n IT Business Information Solution"""
body = start + list_files + end
client_msg.attach(MIMEText(body, 'html'))
client_msg_subject = "[SUCCESS] LUXIA - FastQ transfer files"
client_msg = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ' '.join(client)+ "CC: %s\r\n" % ','.join(ibbl)+ "Subject: %s\r\n" % client_msg_subject+ "\r\n"+ body
toSuccess = client + ibbl
#message_success = client_msg.as_string()

# No Files
bis_msg = MIMEMultipart()
#bis_msg['From'] = fromaddr
#bis_msg['To'] = ','.join(bis)
#bis_msg['CC'] =','.join(bisCC)
#bis_msg['Subject'] = "[INFO] LUXIA - FastQ transfer files"
body = """Dear IT Team,\r\n \r\n The automatic script for LUXIA files transfer ran well. But there is no files to transfer.\r\n \r\n Regards.\r\n IT Business Information Solution"""
bis_msg.attach(MIMEText(body, 'html'))

bis_msg_subject =  "[INFO] LUXIA - FastQ transfer files"
bis_msg = "From: %s\r\n" % fromaddr + "To: %s\r\n" % ','.join(bis)+ "Subject: %s\r\n" % bis_msg_subject+ "\r\n"+ body
toaddrs = bis
#message_no_files = bis_msg.as_string()


