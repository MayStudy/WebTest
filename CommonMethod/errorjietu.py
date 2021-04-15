import os
from datetime import time

from selenium import webdriver
from time import sleep, strftime, localtime,time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        # self.driver.save_screenshot('baidu.png')
        #截图加上时间
        st=strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))
        filename = st + '.png'
        # self.driver.save_screenshot(filename)

        path = os.path.abspath('../screenshot')
        file_path = path + '/' + filename
        self.driver.get_screenshot_as_file(file_path)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    case.test1()