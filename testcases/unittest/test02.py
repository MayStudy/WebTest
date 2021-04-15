import unittest
from selenium import webdriver
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass....')
    def setUp(self) -> None:
        print('setup....')

    def tearDown(self) -> None:
        print('teardown....')
    def test01(self):
        print('test01')
    def test02(self):
        print('test02')


    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass....')
if __name__ == '__main__':
    unittest.main()