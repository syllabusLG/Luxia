#!/usr/bin/env python3
import sys
import os
import logging
from logging.handlers import RotatingFileHandler

try:
    from library.functions import *
    from conf.utils import *
except FileNotFoundError as e:
    e, = e.args
    print("'{}' is missing.".format(str(e)))
    sys.exit(1)

log_path = '/home/robot/logs/LUXIA/Luxia_ftp_transfer.log'
# Tests
#path=cas1
#path=cas2
#path=cas3
#path=cas4
#path=cas5
#path=cas6

if __name__ == "__main__":


    """Log all kind of informations"""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler(log_path, 'a', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    """Check if the folder exists"""
    if os.path.exists(path):
        logger.info('Folder ' + path + ' exists')
    else:
        # send email to prevent BIS that transfer forlder doesn't exists
        message = 'Email sent to {} : Folder does not exists'
        exit_with_error_mail(host, port, fromaddr, toHelpdesk, folder_msg, message, logger.error)

    """Check empty folder"""
    if folder_is_not_empty(path):
        logger.info('Folder is not empty')
    else:
        # send email to prevent BIS that there is no files in the folder
        message = 'Email sent to {} : The script ran well, but there is no files to transfer.'
        exit_with_error_mail(host, port, fromaddr, toaddrs, bis_msg, message, logger.warning)

    """Check if files are luxia files"""
    if check_file(path):
        logger.info('Files are Luxia files')
    else:
        # send email to prevent BIOREF that files are not only Luxia files
        message = 'Email sent to {} : not only Luxia files in folder'
        exit_with_error_mail(host, port, fromaddr, toBio2, biorep_msg2, message, logger.error)

    """Check if files extensions are correct"""
    if check_extension(path):
        logger.info('Files extensions are correct')
    else:
        # send email to prevent BIOREF that files extensions are wrong
        message = 'Email sent to {} : files extension incorrect'
        exit_with_error_mail(host, port, fromaddr, toBio2, biorep_msg2, message, logger.error)

    """Check if the number of files is even"""
    if is_files_pair(path):
        logger.info('Number of files is even')
    else:
        # send email to prevent bioref that there are missing files
        message = 'Email sent to {} : some files are missing (number of files is ODD)'
        exit_with_error_mail(host, port, fromaddr, toBio, biorep_msg, message, logger.error)

    """Check if files contain the right R1 and R2"""
    if check_number_file_r1_r2(path):
        logger.info('Files are fine now you can start the transfer')
    else:
        # send email to prevent bioref that there are missing files
        message = 'Email sent to {} : some files are missing (some R1/R2 files are missing)'
        exit_with_error_mail(host, port, fromaddr, toBio, biorep_msg, message, logger.error)

    #Generate check sum
    check_sum_file = check_sum(path)
    logger.info('Checksum file created')

    """connect to Luxia SFTP server"""
    print(myHostName, myUsername, keyFile, path, check_sum_file)
    if connect_to_sftp(myHostName, myUsername, keyFile, path, check_sum_file):
        # transfer files to Luxia
        sendMail(host, port, fromaddr, toSuccess, client_msg)
        # FTP Success
        logger.info('FTP : transfer success')
        # Delete Files
        deleteFile(path)
        logger.info('Files have been deleted')
    else:
        # send email to prevent that transfer is failed
        message = 'Email sent to {} : cannot access to the FTP server'
        exit_with_error_mail(host, port, fromaddr, toFtp, ftp_msg, message, logger.error)

    
