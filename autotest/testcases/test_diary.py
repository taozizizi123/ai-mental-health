import allure
from api.diary_api import DiaryApi  
from core.assertion import assert_code

@allure.feature("日记模块")
class TestDiary:
    @allure.story("新增日记")
    def test_add(self, user_token):
        res = DiaryApi.add_diary(user_token, "今日开心", "happy")
        assert_code(res)

    @allure.story("日记列表")
    def test_list(self, user_token):
        res = DiaryApi.list_diary(user_token)
        assert_code(res)