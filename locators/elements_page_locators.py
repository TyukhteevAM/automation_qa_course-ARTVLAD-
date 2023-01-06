from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    pass

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    PAGINATOR = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    PENCIL_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    # delete
    DELETE_TITLE = (By.CSS_SELECTOR, 'div[class="rt-noData"]')


class ButtonsPageLocators:
    DOUBLE_BUTTON_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOAD_FILE_NAME = (By.CSS_SELECTOR, 'p[id = "uploadedFilePath"]')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id = "downloadButton"]')
