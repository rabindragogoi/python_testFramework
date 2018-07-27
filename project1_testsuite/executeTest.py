import unittest

from project1_testsuite.logger import get_logging
LOGGER = get_logging()

class Play_Test():
    def __init__(self):
        self.smoke = 'smoke'
        self.regression = 'regression'

    def initiate_test(self,testType):
        if testType == self.smoke:
            self.smoke_test()
        elif testType == self.regression:
            self.regression_test()


    def smoke_test(self):

        from project1_testsuite.smoke.smokeTest import test_smoke
        tc = unittest.TestLoader().loadTestsFromTestCase(test_smoke)
        testSuite = unittest.TestSuite([tc])
        unittest.TextTestRunner(verbosity=2).run(testSuite)

    def regression_test(self):
        from project1_testsuite.regression.regressionTest import test_regression
        tc = unittest.TestLoader().loadTestsFromTestCase(test_regression)
        testSuite = unittest.TestSuite([tc])
        unittest.TextTestRunner(verbosity=2).run(testSuite)




