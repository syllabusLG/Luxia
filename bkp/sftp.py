import pysftp
import os
from paramiko import AuthenticationException

def check_extension(folder):
    files = os.listdir(folder)
    print(len(os.listdir(folder)))
    for file in files:
        list_file, extensions = os.path.splitext(file)
        if "gz" not in extensions:
            return False
        if ".fastq" not in list_file:
            return False
    return True


def check_number_file_r1_r2(folder):
    list_r1 = []
    list_r2 = []
    nbr_file = len(os.listdir(folder))
    
    if nbr_file % 2 != 0:
        return False
    
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

# def check_sum(folder):


def connect_to_sftp(host_name, user, key):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    
    try:
        with pysftp.Connection(host=host_name, username=user, private_key=key, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ...", sftp.pwd)
            # print(local+"*.fastq.gz")
            # sftp.put(local, sftp.pwd)
    except AuthenticationException:
        print("Authentication failed")
        # send email

