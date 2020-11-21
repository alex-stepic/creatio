from .base import BasePage
from .locators import ProjectPageLocators
import time

class ProjectPage(BasePage):
    def status_check(self):

        while not self.is_element_present(*ProjectPageLocators.STATUS):
            time.sleep(1)
        status=self.browser.find_element(*ProjectPageLocators.STATUS)
        time.sleep(1)
        xclass=status.get_attribute("class")
        assert "base-edit-disabled" in xclass, \
            f"Статус.Expect - Поле заблокировано(class=< ...base-edit-disabled>).\n" \
            f"       Real - не заблокировано(class=<{xclass}>)"
