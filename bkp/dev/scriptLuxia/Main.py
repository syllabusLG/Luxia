import sys

try:
    from functions import *
    from utils import *
except FileNotFoundError as e:
    e, = e.args
    print("'{}' is missing.".format(str(e)))
    sys.exit(1)

if __name__ == "__main__":
    """Check if files are luxia files"""
    if check_file(local1):
        print("Files are Luxia files")
    else:
        # send email to prevent bioref that files are not Luxia files
        sendMail(host,port, sender, client_receivers_test, message_to_bioref)
        sys.exit(1)
    """Check if files extensions are correct"""
    if check_extension(local1):
        print("Files extensions are correct")
    else:
        # send email to prevent bioref that files extensions are wrong
        sendMail(host, port, sender, client_receivers_test, message_to_bioref)
        sys.exit(1)
    """Check if files contain the right R1 and R2"""
    if check_number_file_r1_r2(local1):
        print("Files are fine now you can start the transfer")
    else:
        # send email to prevent bioref that there are missing files
        sendMail(host, port, sender, client_receivers_test, message_to_bioref)
        sys.exit(1)

    """connect to Luxia SFTP server"""
    if connect_to_sftp(myHostName, myUsername, keyFile, local1):
        # Generate the check sum
        # check_sum(local1)
        # transfer files to Luxia
        sendMail(host, port, sender, client_receivers_test, message_success)



