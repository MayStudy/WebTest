from selenium import webdriver
from time import sleep
import os
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/alert.html'
        self.driver.get(file_path)
    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to_alert()
        print(alert.text)
        sleep(3)
        alert.accept()
        self.driver.quit()
    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to_alert()
        print(confirm.text)
        sleep(3)
        confirm.accept()
        self.driver.quit()
    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        sleep(3)
        prompt = self.driver.switch_to_alert()
        print(prompt.text)
        prompt.accept()
        sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()