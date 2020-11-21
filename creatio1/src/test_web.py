import json
import pytest
from selenium import webdriver
from src.pages.login import LoginPage
from src.pages.main import MainPage

with open('src/global.json','r', encoding="utf-8") as f:
    data = json.loads(f.read())
    link = data["link"]
    link_main = data["link_main"]
    user_name = data["user_name"]
    password = data["password"]

    print(link)
    print(password)

@pytest.fixture(scope="module")
def browser():
    # Инициализация ChromeDriver
    browser = webdriver.Chrome()
    # driver = Chrome()
    page = LoginPage(browser, link)
    page.open()
    page.login_user(user_name, password)

    yield browser
    browser.quit()

def test_dell_all(browser):

    page = MainPage(browser, link_main)
    page.open()
    page=page.go_to_sales_page()
    page.select_all()
    page.all_del_check()

def test_new_project_status(browser):

    page = MainPage(browser, link_main)
    page.open()
    page=page.go_to_project_list_page()
    page=page.add_project()
    page.status_check()
