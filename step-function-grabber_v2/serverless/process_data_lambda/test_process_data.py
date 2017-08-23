"""unit tests"""
import unittest
import json
import pandas as pd
import process_data


class TestProcessData(unittest.TestCase):
    """test process data"""

    def test_convert_time(self):
        """test process data"""
        time_string = "6:00:00 PM"
        expected_result = "13:00:00"
        result = process_data.convert_time(time_string)
        self.assertEqual(result, expected_result)

    def test_process_data(self):
        """test process data"""
        with open('sample_event.json') as json_data:
            event = json.load(json_data)
        context = {}
        response = process_data.process_data(event, context)
        result = response['dataframe'][['sunrise', 'sunset']]
        sample_output = pd.read_csv('sample_output.csv')
        expected_result = sample_output[['sunrise', 'sunset']]
        result.to_csv('actual_output.csv', index=False)
        self.assertTrue(result.equals(expected_result))

if __name__ == '__main__':
    unittest.main()
