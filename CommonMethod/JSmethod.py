from selenium import webdriver
from time import sleep
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to_alert().accept()
        self.driver.quit()
    def test2(self):
        js='return document.title'

        title=self.driver.execute_script(js)
        sleep(2)
        print(title)
        self.driver.quit()
    def test3(self):
        js = 'var q = document.getElementById("kw");q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(3)
        self.driver.quit()
    #滚动到底部
    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js='window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    # case.test3()
    case.test4()