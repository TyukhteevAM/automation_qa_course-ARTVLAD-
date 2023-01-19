import time
import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgressBarLocators, TabsPageLocators, ToolTipsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for i in remove_button_list:
            i.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    #
    # """не кликается кнопка удаления всех цветов"""
    # def remove_all_values_from_multi(self):
    #     # count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
    #     self.element_is_present(self.locators.MULTI_VALUE_ALL_REMOVE).click()
    #     count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
    #     return count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DataPickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def set_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def check_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.START_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 6))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

    def check_reset_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        start_and_stop_bar_button = self.element_is_clickable(self.locators.START_BUTTON)
        start_and_stop_bar_button.click()
        time.sleep(13)
        reset_bar_button = self.element_is_clickable(self.locators.RESET_BUTTON)
        reset_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.WHAT_TAB,
                     'content': self.locators.WHAT_TAB_TEXT},
                'origin':
                    {'title': self.locators.ORIGIN_TAB,
                     'content': self.locators.ORIGIN_TAB_TEXT},
                'use':
                    {'title': self.locators.USE_TAB,
                     'content': self.locators.USE_TAB_TEXT},
                'more':
                    {'title': self.locators.MORE_TAB,
                     'content': self.locators.MORE_TAB_TEXT},
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        tab_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(tab_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section







