import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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

    class TestFramesPage:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage:
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', "Nested frame does not exist"
            assert child_text == 'Child Iframe', "Nested frame does not exist"

    class TestModalDialogsPage:
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1], "Text from small dialog is less than text from large dailog"
            assert small[0] == 'Small Modal', "The header is not small modal"
            assert large[0] == 'Large Modal', "The header is not large modal"
