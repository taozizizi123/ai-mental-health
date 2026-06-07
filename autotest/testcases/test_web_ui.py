from playwright.sync_api import Page, expect
import allure

@allure.feature("Web前端页面自动化")
def test_login_page(page: Page):
    # 打开项目前端页面
    page.goto("http://127.0.0.1:5173/login")
    # 输入账号密码
    page.get_by_placeholder("请输入邮箱").fill("test01@163.com")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_role("button", name="登录").click()
    # 断言跳转首页
    expect(page).to_have_url("*/home")