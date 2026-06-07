from core.http_request import http_client

class UserApi:
    @staticmethod
    def login(username, password):
        """登录接口 /user/login"""
        data = {"username": username, "password": password}
        return http_client.send("/user/login", method="POST", data=data)

    @staticmethod
    def register(username, password):
        """注册接口 /user/register"""
        data = {"username": username, "password": password}
        return http_client.send("/user/register", method="POST", data=data)

user_api = UserApi()