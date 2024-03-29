from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_TAB_MESSAGE = (By.CSS_SELECTOR, 'h1[id = "sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'h1[id = "sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_5SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT_TEXT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMT_RESULT_TEXT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FIRST_FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    SECOND_FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
