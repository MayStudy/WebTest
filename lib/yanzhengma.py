e81abd2a12404cea9f8ddd430cfda2ef
from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","my_appId","my_appSecret" )
r.addFilePara("image", "替换为你的文件")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text)