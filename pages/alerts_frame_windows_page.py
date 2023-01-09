import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
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

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_after_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text
        return text_result

    def check_promt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT_TEXT).text
        return text, text_result