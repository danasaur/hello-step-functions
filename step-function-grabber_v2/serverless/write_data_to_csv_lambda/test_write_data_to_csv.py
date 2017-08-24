"""unit tests"""
import unittest
import write_data_to_csv


class TestWriteDataToCsv(unittest.TestCase):
    """test write data"""

    def test_write_data_to_csv(self):
        """test write data"""
        # TO DO: mock s3 call?
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
