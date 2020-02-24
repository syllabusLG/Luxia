import unittest
import sys

try:
    from library.functions import *
    from conf.utils import *
except FileNotFoundError as e:
    e, = e.args
    print("'{}' is missing.".format(str(e)))
    sys.exit(1)


class FunctionTest(unittest.TestCase):

    def test_check_file_OK(self):
        return_code = check_file(local1)
        self.assertTrue(return_code)

    def test_check_file_KO(self):
        return_code = check_file(local2)
        self.assertFalse(return_code)

    def test_check_extension_OK(self):
        return_code = check_extension(local1)
        self.assertTrue(return_code)

    def test_check_extension_KO(self):
        return_code = check_extension(local)
        self.assertFalse(return_code)

    def test_files_pair_OK(self):
        return_code = is_files_pair(local2)
        self.assertTrue(return_code)

    def test_files_pair_KO(self):
        return_code = is_files_pair(local3)
        self.assertFalse(return_code)

    def test_check_number_file_r1_r2_OK(self):
        return_code = check_number_file_r1_r2(local1)
        self.assertTrue(return_code)

    def test_check_number_file_r1_r2_KO(self):
        return_code = check_number_file_r1_r2(local4)
        self.assertFalse(return_code)
