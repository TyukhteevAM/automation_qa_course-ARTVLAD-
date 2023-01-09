import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


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