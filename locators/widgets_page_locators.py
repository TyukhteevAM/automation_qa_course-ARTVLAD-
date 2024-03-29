from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class ="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    # MULTI_VALUE_ALL_REMOVE = (By.CSS_SELECTOR, 'div[class="auto-complete__indicator auto-complete__clear-indicator css-tlfecz-indicatorContainer"] svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')

class DataPickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')

class SliderPageLocators:
    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.XPATH, '// input[@id="sliderValue"]')
    INPUT_SLIDER_RESULT = (By.XPATH, '// input[@id="sliderValue"]')

class ProgressBarLocators:
    START_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    RESET_BUTTON = (By.CSS_SELECTOR, 'button[id="resetButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[role="progressbar"]')

class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    WHAT_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-what"]/p')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    ORIGIN_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-origin"]/p')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    USE_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-use"]/p')
    MORE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    MORE_TAB_TEXT = (By.XPATH, '//a[@id="demo-tabpane-more"]/p')

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')





