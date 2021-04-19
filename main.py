# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
# from util import toolmethod
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.
from selenium import webdriver
from testcases.Gitee_login import TestUserLogin
if __name__ == '__main__':
    case01 = TestUserLogin()
    # case01.test_user_login_username_error()
    case01.test_user_login_ok()


