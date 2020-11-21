from .base import BasePage
from .sales import SalesPage
from .project_list import ProjectListPage
from .locators import MainPageLocators
import time

class MainPage(BasePage):
    def go_to_sales_page(self):

        self.browser.maximize_window()
        while not self.is_element_present(*MainPageLocators.SAlES_BUTTON):
            time.sleep(3)
        link = self.browser.find_element(*MainPageLocators.SAlES_BUTTON)
        link.click()
        return SalesPage(browser=self.browser, url=self.browser.current_url)

    def go_to_project_list_page(self):

        self.browser.maximize_window()
        while not self.is_element_present(*MainPageLocators.PROJECT_LIST_BUTTON):
            time.sleep(3)
        link = self.browser.find_element(*MainPageLocators.PROJECT_LIST_BUTTON)
        link.click()
        return ProjectListPage(browser=self.browser, url=self.browser.current_url)