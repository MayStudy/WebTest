from selenium import webdriver
import os
from time import sleep
class TestCase(object):
    def __init__(self):
        #加载本地文件
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms.html'
        print(file_path)
        self.driver.get(file_path)
    def test_login(self):
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_id('pwd').send_keys('123')
        sleep(2)
        self.driver.find_element_by_id('submit').click()
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    case.test_login()