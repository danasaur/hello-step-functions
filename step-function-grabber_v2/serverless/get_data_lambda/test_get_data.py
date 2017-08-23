"""unit tests"""
import unittest
import get_data


class TestGetData(unittest.TestCase):
    """test get data"""

    def test_get_data(self):
        """test get data"""
        event = {}
        context = {}
        response = get_data.get_data(event, context)
        self.assertEqual(200, response['status'])

if __name__ == '__main__':
    unittest.main()
