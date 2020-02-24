#!/usr/bin/python
import smtplib
import sys
import os

# email Variables
from dataclasses import dataclass
from typing import List


#email Variables
exp="IBBL - LUXIA FastQ File transfer"
sender = 'robot@ibbl.lih.lu'
#client_receivers="contact@luxia-scientific.com"
client_receivers_test="ariane.asselekama@gmail.com"
ibbl_receivers='maria-manuela.tonini@ibbl.lu; lorieza.castillo@ibbl.lu; wim.ammerlaan@ibbl.lu; robot_transfer@ibbl.lu'
ibbl_receivers_test='ariane.assele-kama@ibbl.lu'
helpdesk='helpdesk@ibbl.lu'
subjectOK="[SUCCESS] LUXIA - FastQ transfer files"
subjectKO="[ERROR] LUXIA - FastQ transfer files"

message_to_bis = """From: IBBL - LUXIA FastQ File transfer <robot@ibbl.lih.lu>
To: IBBL BIS Team <IBBLIT@ibbl.lu>
MIME-Version: 1.0
Content-type: text/html
Subject: [ERROR] LUXIA - FastQ transfer files - Folder doesn't exist

Dear BIS Team,

Please have a look on the folder <b>path</b>

It seems that the path doesn't not exist.

No files have been sent to the client.

Regards.
IBBL Business Information Services

"""

message_for_ftp_error = """From: IBBL - LUXIA FastQ File transfer <robot@ibbl.lih.lu>
To: IBBL BIS Team <IBBLIT@ibbl.lu>
MIME-Version: 1.0
Content-type: text/html
Subject: [ERROR] LUXIA - FastQ transfer files

Dear All

Please have a look on the folder <b>path</b>. 

It seems that the $<b>path</b> is not a folder.

No files have been sent to the client."

Regards.
IBBL Business Information Services
"""

message_to_bioref = """From: IBBL - LUXIA FastQ File transfer <robot@ibbl.lih.lu>
To: IBBL BIS Team <IBBLIT@ibbl.lu>
MIME-Version: 1.0
Content-type: text/html
Subject: [ERROR] LUXIA - FastQ transfer files

Dear Client,

There is an error on the file list provide in the folder, for FTP transfer to LUXIA.

Please have a look on the list below to check what's going wrong.

<b>list_files.</b>
            
Regards.
IBBL Business Information Services
"""

message_success = """From: IBBL - LUXIA FastQ File transfer <robot@ibbl.lih.lu>
To: IBBL BIS Team <IBBLIT@ibbl.lu>
MIME-Version: 1.0
Content-type: text/html
Subject: [SUCCESS] LUXIA - FastQ transfer files

Dear All,

Please find below the FastQ files transfered.

<b>list_files.</b>

Regards.
IBBL Business Information Services

"""

print(sys.argv)

path = sys.argv[1]
cas = sys.argv[2]
list_files = sys.argv[3:]
print(list_files)


@dataclass
class MailOptions:
    sender: str
    receivers: List[str]
    message: str


def email_definition():
    switcher = {
        "1": MailOptions(sender, [client_receivers_test], message_to_bis),
        "2": MailOptions(sender, [client_receivers_test], message_for_ftp_error),
        "3": MailOptions(sender, [client_receivers_test], message_to_bioref),
        "4": MailOptions(sender, [client_receivers_test], message_success)
    }
    return switcher.get(cas, "nothing")


if __name__ == '__main__':
    with smtplib.SMTP("smtp.lih.lu", 25) as server:
        definition = email_definition()
        server.sendmail(definition.sender, definition.receivers, definition.message)


