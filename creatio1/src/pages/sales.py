from .base import BasePage
from .locators import SalesPageLocators
import time

class SalesPage(BasePage):
    def select_all(self):
        while not self.is_element_present(*SalesPageLocators.ANY_ROW):
            time.sleep(1)
        menu_item = self.browser.find_element(*SalesPageLocators.ACTIONS_MENU)
        menu_item.click()
        time.sleep(1)
        menu_item = self.browser.find_element(*SalesPageLocators.ACTIONS_MENU_ALL)
        menu_item.click()
        time.sleep(1)
    def all_del_check(self):
        while not self.is_element_present(*SalesPageLocators.GRID_MULTISELECT):
            time.sleep(1)
        menu_item = self.browser.find_element(*SalesPageLocators.ACTIONS_MENU)
        menu_item.click()
        time.sleep(1)
        menu_item = self.browser.find_element(*SalesPageLocators.ACTIONS_MENU_DEL)
        xclass=menu_item.get_attribute("class")

        assert "disabled" in xclass,\
         f"Функция удаления всех записей. Expect - заблокирована(class=< ...-disabled>).\n" \
         f"                               Real- не заблокирована(class=<{xclass}>)>"
