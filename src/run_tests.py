import unittest

import os

loader = unittest.TestLoader()
start_dir = r'C:\msds510-midterm\src\tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
