"""unit tests"""
import unittest
import write_data


class TestWriteData(unittest.TestCase):
    """test write data"""

    def test_write_data(self):
        """test write data"""
        event = {}
        context = {}
        response = write_data.write_data(event, context)
        self.assertEqual(200, response['status'])

if __name__ == '__main__':
    unittest.main()
