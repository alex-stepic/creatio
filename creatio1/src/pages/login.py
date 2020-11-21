from .base import BasePage
from .main import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def login_user(self, name, password):
        if self.is_element_present(*LoginPageLocators.LOGIN_NAME):
            xname = self.browser.find_element(*LoginPageLocators.LOGIN_NAME)
            xname.send_keys(name)

            xpassword = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
            xpassword.send_keys(password)

            xbutton = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
            xbutton.click()
            return MainPage(browser=self.browser, url=self.browser.current_url)

