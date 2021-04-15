from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","360774","e81abd2a12404cea9f8ddd430cfda2ef" )
r.addFilePara("image", "../screenshot/yanzhengma.jpeg")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
# result = res.text
# print(result)
body = res.json()['showapi_res_body']
print(body['Result'])