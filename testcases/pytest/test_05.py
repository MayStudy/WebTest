#pytest的setup和teardown
import pytest
class TestCase01(object):
    @classmethod
    def setup_class(self):
        print('setupclass...')
    @classmethod
    def teardown_class(self):
        print('teardownclass...')
    def test1(self):
        print('test1...class')
    def test2(self):
        print('test2.....')
def setup_function():
    print('setup_function...')
def teardown_function():
    print('teardown_function...')
def setup_module():
    print('setup_module')
def teardown_module():
    print('teardown_module')
def test1():
    print('test1.....')
def test2():
    print('test2.....')
if __name__ == '__main__':
        pytest.main('-sv','test_05.py')