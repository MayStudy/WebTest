from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form3.html'
        self.driver.get(file_path)
    def test_Select(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)
        # select.select_by_index(1)
        # sleep(3)
        # select.select_by_value('bj')
        # sleep(3)
        # select.select_by_visible_text('Shanghai')
        # # sleep(3)
        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(2)
        # sleep(3)
        # select.deselect_all()#反选
        #
        # sleep(3)
        for option in select.options:
            print(option.text)
            sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    case.test_Select()