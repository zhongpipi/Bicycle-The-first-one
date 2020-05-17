import pytest


#
#
# # 参数化，前面两个变量，后面是值
# @pytest.mark.parametrize("test_input,excepted", [("3+5", 8), ("3*4", 12)])
# def test_eval(test_input, excepted):
#     # eval求值
#     assert eval(test_input) == excepted

# @pytest.mark.parametrize("x", [1, 2])
# @pytest.mark.parametrize("y", [3, 8, 9])
# def test_foo(x, y):
#     print(f"测试数据组合：{x}，y：{y}")

#
test_user_data = {'Tom', 'Jerry'}


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入的参数
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user

# indirect=True 可以把传过来的参数当函数使用
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值；{a}")
    assert a != ""
