import unittest
import pandas as pd
import os
from lib import preprocess_data, generate_plot

class TestLibFunctions(unittest.TestCase):

    def test_preprocess_data(self):
        df = preprocess_data()
        # Check if the returned object is a DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        # Check if 'Year' column exists
        self.assertIn('Year', df.columns)
        # Check if DataFrame is not empty
        self.assertFalse(df.empty)
        # Check if all 'Name' entries are 'AAPL'
        self.assertTrue((df['Name'] == 'AAPL').all())

    def test_generate_plot(self):
        # Create a sample DataFrame
        data = {
            'mean': [100, 110, 120],
            'median': [90, 105, 115],
            'std': [5, 10, 8]
        }
        index = [2019, 2020, 2021]
        yearly_stats = pd.DataFrame(data, index=index)

        # Remove 'plot.png' if it exists
        if os.path.exists('plot.png'):
            os.remove('plot.png')

        # Generate plot
        generate_plot(yearly_stats)

        # Check if 'plot.png' was created
        self.assertTrue(os.path.exists('plot.png'))

if __name__ == '__main__':
    unittest.main()
