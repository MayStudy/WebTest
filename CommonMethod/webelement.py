from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
#http://sahitest.com/demo/
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        e1 = WebElement;
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)
        self.driver.quit()
    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    case.test_webelement_method()