from .base import BasePage
from .project import ProjectPage
from .locators import ProjectListLocators
import time

class ProjectListPage(BasePage):
    def add_project(self):
        while not self.is_element_present(*ProjectListLocators.ANY_ROW):
            time.sleep(1)
        menu_item = self.browser.find_element(*ProjectListLocators.ADD)
        menu_item.click()
        return ProjectPage(browser=self.browser, url=self.browser.current_url)

