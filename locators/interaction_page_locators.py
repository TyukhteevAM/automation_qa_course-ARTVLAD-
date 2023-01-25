from selenium.webdriver.common.by import By


class SortablePageLocators:

    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    ITEM_GRID = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

