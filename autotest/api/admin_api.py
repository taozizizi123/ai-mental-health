from core.http_request import http_client

class AdminApi:
    @staticmethod
    def data_overview(token):
        return http_client.send("/admin/overview", method="GET", token=token)

    @staticmethod
    def chat_list(token):
        return http_client.send("/admin/chat/list", method="GET", token=token)