from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
class TestUserLogin(object):
    login_data = [
        ('199','1146975@yaomei'),
        ('19921892292','1146975@yaomei'),
    ]
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://gitee.com/login')
        self.driver.maximize_window()

    # @pytest.mark.parametrize('username,pwd,expected',login_data)
    # def test_user_login(self,username,pwd,expected):
    #     #用户名为空
    #     username = ''
    #     pwd = '1146975@yaomei'
    #     expected = '用户名为必填项'
    #     # errorname=''
    #     self.driver.find_element_by_id('user_login').clear()
    #     self.driver.find_element_by_id('user_login').send_keys(username)
    #     self.driver.find_element_by_id('user_password').clear()
    #     self.driver.find_element_by_id('user_password').send_keys(pwd)
    #     self.driver.find_element_by_name('commit').click()
    #     usernameerror=self.driver.find_element_by_xpath('//*[@id="git-login"]/div')
    #     # print(usernameerror.text)
    #     assert usernameerror.text == expected
    @pytest.mark.parametrize('username,pwd', login_data)
    def test_user_login_ok(self,username,pwd):
        # username = '19921892292'
        # pwd = '1146975@yaomei'
        # expected = '我的工作台 - Gitee.com'
        self.driver.find_element_by_id('user_login').clear()
        self.driver.find_element_by_id('user_login').send_keys(username)
        self.driver.find_element_by_id('user_password').clear()
        self.driver.find_element_by_id('user_password').send_keys(pwd)
        self.driver.find_element_by_name('commit').click()
        # WebDriverWait(self.driver,5).until(EC.title_is(expected))
        # sleep(3)
        # assert self.driver.title == expected
        # self.driver.quit()
if __name__ == '__main__':
    pytest.main(['-sv','Gitee_login.py'])