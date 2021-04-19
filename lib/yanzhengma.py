
from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","272526","a924d4e982ae404b8a068b4d1c7784f2" )
r.addFilePara("image", "yanzhengma.jpeg")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text)