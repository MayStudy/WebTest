from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get('http://sahitest.com/demo/clicks.htm')
    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)
        self.driver.quit()
    def test_key(self):
        self.driver.get('http://www.baidu.com')
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('selenium')
        sleep(2)
        kw.send_keys(Keys.COMMAND,'a')
        sleep(2)
        kw.send_keys(Keys.COMMAND,'x')
        sleep(2)
        kw.send_keys(Keys.COMMAND,'v')
        sleep(2)
        self.driver.quit()



if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.test_key()