from core.http_request import http_client

class ChatApi:
    @staticmethod
    def create_session(token, session_title="测试会话"):
        """新建对话会话"""
        data = {"sessionTitle": session_title}
        return http_client.send("/psychological-chat/sessions/start", method="POST", data=data, token=token)

    @staticmethod
    def send_msg(token, session_id, user_input):
        """发送AI提问消息"""
        data = {"sessionId": session_id, "userInput": user_input}
        return http_client.send("/psychological-chat/stream", method="POST", data=data, token=token)

chat_api = ChatApi()