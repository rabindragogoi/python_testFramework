import unittest
from project1_testsuite.logger import get_logging
LOGGER = get_logging()
class test_smoke(unittest.TestCase):
    def test_smoke(self):
        LOGGER.info("Smoke test is running")
        self.assertEqual(5,5)
        sysvar = "The os is loaded in C:\\ drive"



