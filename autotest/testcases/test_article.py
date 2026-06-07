import allure
from api.article_api import ArticleApi
from core.assertion import assert_code

@allure.feature("文章知识库")
class TestArticle:
    def test_art_list(self, user_token):
        res = ArticleApi.get_list(user_token)
        assert_code(res)

    def test_art_detail(self, user_token):
        res = ArticleApi.get_detail(user_token, 1)
        assert_code(res)