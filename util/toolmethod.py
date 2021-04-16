import string
import time
from random import randrange
import random

from selenium import webdriver
from lib.ShowapiRequest import ShowapiRequest
from PIL import Image
import os
def get_code(driver,id):
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshot'
    picture_name1 = path + '\\' + str(t) + '.png'
    driver.save_screenshot(picture_name1)
    ce=driver.find_element_by_id(id)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    dpr = driver.execute_script('return window.devicePixelRatio')
    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop(left*dpr,top*dpr,right*dpr,height*dpr)
    # im = Image.open(picture_name1)
    # img = im.crop(left,top,right,height)
    t = time.time()
    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)

    r = ShowapiRequest("http://route.showapi.com/184-4", "360774", "e81abd2a12404cea9f8ddd430cfda2ef")
    r.addFilePara("image", "../screenshot/yanzhengma.jpeg")
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    result = res.text
    print(result)
    body = res.json()['showapi_res_body']
    code = body['Result']
    return code
    driver.quit()
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits,8))
    return rand_str
    driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://test-sso-java.seedland.cc/login')
    get_code(driver,'vcode')
    # gen_random_str()