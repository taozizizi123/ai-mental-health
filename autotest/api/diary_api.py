from core.http_request import http_client

class DiaryApi:
    @staticmethod
    def add_diary(token, content, mood):
        data = {"content": content, "mood": mood}
        return http_client.send("/emotion-diary", method="POST", data=data, token=token)

    @staticmethod
    def get_list(token):
        # 需要根据实际API调整
        return http_client.send("/emotion-diary/list", method="GET", token=token)