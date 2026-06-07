import pytest
import yaml
import os
from api.user_api import user_api

def get_config():
    """获取配置"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config", "env.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session",autouse=True)
def init_env():
    """全局前置初始化"""
    print("====自动化测试环境初始化完成====")
    yield
    print("====自动化用例执行完毕====")

@pytest.fixture(scope="session")
def user_token():
    """获取用户token"""
    env = get_config()
    res = user_api.login(env["test_user"]["account"], env["test_user"]["pwd"])
    if res and res.status_code == 200:
        return res.json().get("token")
    return None

@pytest.fixture(scope="session")
def admin_token():
    """获取管理员token"""
    env = get_config()
    res = user_api.login(env["admin_user"]["account"], env["admin_user"]["pwd"])
    if res and res.status_code == 200:
        return res.json().get("token")
    return None