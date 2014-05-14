'''Unit test for test_data_compute.py

This program tests the output computed by data_compute.compute_company_data
with output getting compared with Expected output.
'''

import data_compute
import unittest

class ExpectedOutput(unittest.TestCase):
    output_values = ( ['A', '1991', 'Dec', '240'],
                      ['B', '1991', 'Sep', '300'],
                      ['C', '1991', 'Jul', '200'],
                      ['D', '1991', 'May', '101']                     
                     )

    def test_to_roman_known_values(self):
        '''compute_company_data should give known result as output_values'''
        result = data_compute.compute_company_data('input_data.csv')
        self.assertEqual(list(self.output_values), result)

if __name__ == '__main__':
    unittest.main()
