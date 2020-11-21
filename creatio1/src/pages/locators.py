from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_NAME = (By.CSS_SELECTOR, "input#loginEdit-el")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#passwordEdit-el")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "span[data-item-marker=btnLogin]")

class MainPageLocators():
    SAlES_BUTTON = (By.CSS_SELECTOR, "div.content-panel a[data-item-marker=Продажи]")
    PROJECT_LIST_BUTTON = (By.CSS_SELECTOR, "div.content-panel a[data-item-marker=Проекты]")

class SalesPageLocators():
    ACTIONS_MENU = (By.CSS_SELECTOR, "[data-item-marker=SeparateModeActionsButton]")
    ACTIONS_MENU_ALL=(By.CSS_SELECTOR,'li.menu-item[data-item-marker = "Выбрать все"]')
    ACTIONS_MENU_DEL = (By.CSS_SELECTOR, 'li.menu-item[data-item-marker = "Удалить"]')
    ANY_ROW  =(By.CSS_SELECTOR, 'div.grid-row.grid-module')
    GRID_MULTISELECT  =(By.CSS_SELECTOR, 'div.grid.grid-tiled.grid-multiselect')

class ProjectListLocators():
    ANY_ROW = (By.CSS_SELECTOR, 'div.grid-row.grid-module')
    ADD = (By.CSS_SELECTOR, "[data-item-marker=SeparateModeAddRecordButton]")

class ProjectPageLocators():
    STATUS=(By.CSS_SELECTOR, "div[data-item-marker='Status Состояние']")

