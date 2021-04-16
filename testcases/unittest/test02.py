import unittest
from selenium import webdriver
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass....')
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()

    def setUp(self) -> None:
        print('setup....')
        self.assertEqual(1,1)
        self.assertIn(10,[1,2,3])

    def tearDown(self) -> None:
        print('teardown....')

    def test01(self):
        print('test01')
        self.driver.find_element_by_id('kw').send_keys('bala')

    def test02(self):
        print('test02')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass....')
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main()