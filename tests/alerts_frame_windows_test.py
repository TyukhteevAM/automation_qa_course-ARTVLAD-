import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:
    class TestBrowserWindow:

        def test_new_tab(self, driver):
            browser_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_tab_page.open()
            text_result = browser_tab_page.check_new_tab()
            assert text_result == "This is a sample page", "New tab has not been opened"

        def test_new_window(self, driver):
            browser_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_tab_page.open()
            text_result = browser_tab_page.check_new_window()
            assert text_result == "This is a sample page", "New window has not been opened"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert = alert_page.check_see_alert()
            assert alert == "You clicked a button", "Alert did not show up"

        def test_see_alert_after_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert = alert_page.check_see_alert_after_5_sec()
            assert alert == "This alert appeared after 5 seconds", "Alert did not show up"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert did not show up"

        def test_promt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_promt_alert()
            assert text in alert_text, "Alert did not show up"

