import unittest
import HtmlTestRunner
from orangehrm.pom.tests.testcases import Logintest


class TestSuite:
    tc1 = unittest.TestLoader().loadTestsFromTestCase(Logintest)

    smoketest = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=1).run(smoketest)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/PythonSelenium/reports'))
