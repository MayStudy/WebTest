import pytest
'''
username,password
1.admin xxx
2.xxx 123
3.admin 123
4.xxx xxx

'''
data = ['123','456']
@pytest.mark.parametrize('pwd',data)
def test1(pwd):
    print(pwd)
#元组
data2=[
    (1,2,3),
    (4,5,6)
]
@pytest.mark.parametrize('a,b,c',data2)
def test1(a,b,c):
    print(a,b,c)

#字典
data3 = (
    {
    'user':1,
    'pwd':2
    },
    {
        'age':3,
        'email':"111@qq.com"
    }
)
@pytest.mark.parametrize('dic',data3)
def test1(dic):
    print(dic)

data_1=[
    pytest.param(1,2,3,id="(a+b):pass"),
    pytest.param(4,5,10,id="(a+b):fail")
]
def add(a,b):
    return a+b
class TestParametrize(object):
    @pytest.mark.parametrize('a,b,expect',data_1)
    def test_parametrize_1(self,a,b,expect):
        assert add(a,b) == expect

# if __name__ == '__main__':
#     pytest.main()