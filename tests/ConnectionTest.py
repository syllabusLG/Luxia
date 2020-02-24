import unittest
# try:
#     from functions import *
#     from utils import *
# except FileNotFoundError as e:
#     e, = e.args
#     print("'{}' is missing.".format(str(e)))
#     sys.exit(1)
from library.functions import connect_to_sftp
from conf.utils import myHostName, myUsername, keyFile, local1, KeyFileWrong


class SftpConnectionTest(unittest.TestCase):

    def test_sftp_OK(self):
        return_code = connect_to_sftp(myHostName, myUsername, keyFile, local1)
        self.assertTrue(return_code)

    def test_sftp_KO(self):
        return_code = connect_to_sftp(myHostName, myUsername, KeyFileWrong, local1)
        self.assertFalse(return_code)

