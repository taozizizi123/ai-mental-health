from core.http_request import http_client

class ArticleApi:
    @staticmethod
    def get_list(token):
        return http_client.send("/knowledge/article/page", method="GET", token=token)

    @staticmethod
    def get_detail(token, id):
        return http_client.send(f"/knowledge/article/{id}", method="GET", token=token)