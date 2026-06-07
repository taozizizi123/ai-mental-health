import allure
import yaml
import os
from api.user_api import user_api
from core.assertion import assert_code, assert_json_key

# 获取当前文件所在目录，确保配置文件路径正确
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(current_dir, "config", "env.yaml")

with open(config_path,"r",encoding="utf-8") as f:
    env = yaml.safe_load(f)
user_acc = env["test_user"]["account"]
user_pwd = env["test_user"]["pwd"]

@allure.feature("用户模块自动化")
class TestUser:
    @allure.story("正常登录")
    def test_login_success(self):
        res = user_api.login(user_acc, user_pwd)
        assert_code(res)
        assert_json_key(res,"token")

    @allure.story("密码错误登录失败")
    def test_login_err_pwd(self):
        res = user_api.login(user_acc,"654321")
        assert_code(res, expect_code=400)