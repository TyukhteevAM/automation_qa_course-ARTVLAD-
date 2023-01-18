import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePage:

        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before > count_value_after

        # """не кликается кнопка удаления всех цветов"""
        # def test_remove_all_values_from_multi(self, driver):
        #     auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        #     auto_complete_page.open()
        #     auto_complete_page.fill_input_multi()
        #     # time.sleep(3)
        #     count_value_after = auto_complete_page.remove_all_values_from_multi()
        #     print(count_value_after)
        #     # assert count_value_after == 0

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'the added colors are missing in the input'

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'the date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'the date and time have not been changed'

    class TestSliderPage:
        def test_check_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.set_slider_value()
            assert before != after, "The slide bar has not been changed"

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.check_progress_bar()
            assert before != after, "The progress bar has not been changed"

        def test_reset_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.check_reset_progress_bar()
            assert f'{before}%' == after, "The progress bar has not been reseted"
