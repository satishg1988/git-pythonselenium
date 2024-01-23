import unittest
import HtmlTestRunner
from abhibus.pom.tests.testcases import TestCases


class TestSuite:
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCases)

    smoketest = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=1).run(smoketest)


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/PythonSelenium/reports'))
