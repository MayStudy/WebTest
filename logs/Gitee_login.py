from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util.toolmethod import get_logger
import pytest
class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gitee.com/login')
        self.driver.maximize_window()
        self.logger = get_logger()
        self.logger.info('测试用户登录')
    def test_user_login_username_error(self):
        #用户名为空
        username = ''
        pwd = '1146975@yaomei'
        expected = '用户名为必填项'
        # errorname=''
        self.driver.find_element_by_id('user_login').clear()
        self.driver.find_element_by_id('user_login').send_keys(username)
        self.logger.debug('输入用户名称：%s',username)
        self.driver.find_element_by_id('user_password').clear()
        self.driver.find_element_by_id('user_password').send_keys(pwd)
        self.logger.debug('输入密码：%s', pwd)
        self.driver.find_element_by_name('commit').click()
        self.logger.debug('点击登录')
        usernameerror = self.driver.find_element_by_xpath('//*[@id="git-login"]/div')
        # print(usernameerror.text)
        try:
            assert usernameerror.text == expected
        except AttributeError as ae:
            self.logger.error("login,登录:%s", "报错了", exc_info=1)
    def test_user_login_ok(self):
        username = '19921892292'
        pwd = '1146975@yaomei'
        expected = '我的工作台 - Gitee.com'
        self.driver.find_element_by_id('user_login').clear()
        self.driver.find_element_by_id('user_login').send_keys(username)
        self.logger.debug('输入用户名称：%s', username)
        self.driver.find_element_by_id('user_password').clear()
        self.driver.find_element_by_id('user_password').send_keys(pwd)
        self.logger.debug('输入密码：%s', pwd)
        self.driver.find_element_by_name('commit').click()
        self.logger.debug('点击登录')
        WebDriverWait(self.driver,5).until(EC.title_is(expected))
        sleep(3)
        try:
            assert self.driver.title == expected
        except AttributeError as ae:
            self.logger.error("login,登录:%s", "报错了", exc_info=1)
        self.driver.quit()
if __name__ == '__main__':
    pytest.main(['Gitee_login.py'])