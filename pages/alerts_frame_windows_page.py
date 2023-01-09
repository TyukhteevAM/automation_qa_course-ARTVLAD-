from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_tab()
        text_title = self.element_is_present(self.locators.NEW_TAB_MESSAGE).text
        return text_title

    def check_new_window(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_tab()
        text_title = self.element_is_present(self.locators.NEW_TAB_MESSAGE).text
        return text_title