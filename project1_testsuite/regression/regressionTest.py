import unittest
from project1_testsuite.logger import get_logging
LOGGER = get_logging()

class test_regression(unittest.TestCase):
    def test_smoke(self):
        LOGGER.info("Regression test is running")
        self.assertEqual(5,5)

