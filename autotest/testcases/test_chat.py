import allure
from api.user_api import user_api
from api.chat_api import chat_api
from core.assertion import assert_code, assert_json_key

@allure.feature("AI心理对话模块")
class TestChat:
    def setup_class(self):
        # 前置：登录获取token
        login_res = user_api.login("test01@163.com","123456")
        self.token = login_res.json()["token"]

    @allure.story("创建对话会话")
    def test_create_session(self):
        res = chat_api.create_session(self.token)
        assert_code(res)
        self.session_id = res.json()["sessionId"]
        assert_json_key(res,"sessionId")

    @allure.story("发送聊天消息，AI返回内容")
    def test_ai_reply(self):
        res = chat_api.send_msg(self.token,self.session_id,"我最近情绪低落怎么办")
        assert_code(res)
        assert_json_key(res,"reply")