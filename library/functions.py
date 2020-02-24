import pysftp
import os
import shutil
import smtplib
import email
import hashlib

import sys
from paramiko import AuthenticationException
from pysftp import CredentialException
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def folder_is_not_empty(folder):
    files = os.listdir(folder)
    if len(files) != 0:
       return True
    else:
       return False

def check_extension(folder):
    files = os.listdir(folder)
    for file in files:
        list_file, extensions = os.path.splitext(file)
        if "gz" not in extensions:
            return False
        if ".fastq" not in list_file:
            return False
    return True


def is_files_pair(folder):
    nbr_file = len(os.listdir(folder))
    if nbr_file % 2 != 0:
        return False
    else:
        return True


def check_number_file_r1_r2(folder):
    list_r1 = []
    list_r2 = []
    files = os.listdir(folder)
    for file in files:
        if "R1_001" in file:
            list_r1.append(file)
        if "R2_001" in file:
            list_r2.append(file)
    if len(list_r1) != len(list_r2):
        return False
    return True


def check_file(folder):
    files = os.listdir(folder)
    print(files)
    for file in files:
        if "LX" not in file:
            return False
    return True


def check_sum(folder):
    my_file = open(folder+"luxia_list.md5", "w+")
    files = os.listdir(folder)
    hash_md5 = hashlib.md5()
    for file in files:
       with open(folder+file, "rb") as f:
          for chunk in iter(lambda: f.read(), b""):
             hash_md5.update(chunk)
             my_file.write(str(hash_md5.hexdigest())+" "+str(file)+"\r\n")
    my_file.close()
    return hash_md5.hexdigest()


def connect_to_sftp(host_name, user, key, folder, check_sum_file):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        with pysftp.Connection(host=host_name, username=user, private_key=key, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ...", sftp.pwd)
            # Tests
            #with sftp.cd('test'):
            #print(sftp.pwd)
            files = os.listdir(folder)
            for file in files:
                print(file)
                sftp.put(folder+file)
            #sftp.put(check_sum_file)
            sftp.close()
            return True
    except (AuthenticationException, CredentialException, FileNotFoundError):
        print("Authentication failed")
        return False


def deleteFile(folder):
    files = os.listdir(folder)
    try:
       for file in files:
           os.remove(folder+file)
           #shutil.move(folder+file, folderMove+file)
       return True
    except FileNotFoundError:
       return False 


def sendMail(server, port, sender, receivers, msg):
    with smtplib.SMTP(server, port) as server:
        server.sendmail(sender, receivers, msg)


def exit_with_error_mail(server, port, sender, receivers, mail_msg, log_msg: str, log_fn) -> None:
    sendMail(server, port, sender, receivers, mail_msg)
    log_fn(log_msg.format(str(receivers)))
    sys.exit(1)



