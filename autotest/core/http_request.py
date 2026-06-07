import requests
import yaml
import os
from core.logger import get_logger

logger = get_logger()
# 获取当前文件所在目录，确保配置文件路径正确
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(current_dir, "config", "env.yaml")

# 读取配置
with open(config_path, "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)
BASE_URL = cfg["base_url"]
TIMEOUT = cfg["timeout"]

class HttpRequest:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"Content-Type": "application/json"}

    def send(self, uri, method="GET", data=None, params=None, token=None):
        """统一发送请求"""
        url = BASE_URL + uri
        # 创建临时 headers 副本，避免污染实例变量
        headers = self.headers.copy()
        if token:
            headers["token"] = token
        try:
            if method.upper() == "GET":
                res = self.session.get(url=url, headers=headers, params=params, timeout=TIMEOUT)
            elif method.upper() == "POST":
                res = self.session.post(url=url, headers=headers, json=data, timeout=TIMEOUT)
            elif method.upper() == "DELETE":
                res = self.session.delete(url=url, headers=headers, json=data, timeout=TIMEOUT)
            else:
                raise Exception("请求方法错误")
            logger.info(f"接口:{uri},状态码:{res.status_code},返回:{res.text[:300]}")
            return res
        except Exception as e:
            logger.error(f"接口{uri}请求异常:{str(e)}")
            return None

# 全局请求实例
http_client = HttpRequest()