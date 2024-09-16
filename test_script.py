# test_script.py

import unittest
import subprocess
import os

class TestScript(unittest.TestCase):

    def test_script_execution(self):
        # Remove 'plot.png' if it exists
        if os.path.exists('plot.png'):
            os.remove('plot.png')

        # Run the script and capture output
        result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)

        # Check if script ran successfully
        self.assertEqual(result.returncode, 0)

        # Check if 'plot.png' was created
        self.assertTrue(os.path.exists('plot.png'))

        # Optionally, check for specific output in stdout
        # self.assertIn('Expected Output', result.stdout)

if __name__ == '__main__':
    unittest.main()
