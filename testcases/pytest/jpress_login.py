from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import toolmethod
class TestUserLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://42.192.20.182:8080/user/login')
        self.driver.maximize_window()
    #测试验证码错误
    def test_login_error(self):
        username = ''
        pwd = '123456'
        expected = '账号不能为空'
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_class_name('btn').click()
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        assert alert.text == expected
        alert.accept()
        sleep(5)
        # self.driver.quit()
    def test_login_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = '用户中心'
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_class_name('btn').click()
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        assert self.driver.title == expected
        sleep(5)
        self.driver.quit()