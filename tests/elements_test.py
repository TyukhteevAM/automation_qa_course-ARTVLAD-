import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:

        @allure.title("Check Text Box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page. \
                check_filled_form()
            assert full_name == output_name, "name does not match"
            assert email == output_email, "email does not match"
            assert current_address == output_current_address, "current_address does not match"
            assert permanent_address == permanent_address, "permanent_address does not match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check Check Box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check_box_page.get_checked_checkboxes()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check Radio Button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()  # получаем ошибку, т.к. на клиенте невозможно выбрать этот радиобаттон
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    @allure.feature("WebTable")
    class TestWebTable:

        @allure.title("Check web table add_person")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        @allure.title("Check web table search person")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_people(key_word)
            time.sleep(2)  # периодически тест падает, в поле поиска не отображается key_word и срабатывает assert
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person wasn't found in the table"

        @allure.title("Check web table update person info")
        def test_web_table_update_person_inf0(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has noi been changed"

        @allure.title("Check web table delete person")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_people(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title("Check web table change count row")
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "The numbers in the table has not been changed or has changed incorrectly"

    @allure.feature("Buttons")
    class TestButtonsPage:

        @allure.title("Check different click on the buttons")
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            once = button_page.click_on_different_button("once")
            assert double == "You have done a double click", "The double click button was no pressed"
            assert right == "You have done a right click", "The right click button was no pressed"
            assert once == "You have done a dynamic click", "The once click button was no pressed"

    @allure.feature("Links")
    class TestLinksPage:

        @allure.title("Check link")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title("Check broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "the link works or the status code in son 400"

    @allure.feature("Upload And Download")
    class TestUploadAndDownloadPage:

        @allure.title("Check upload file")
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "The file has not been uploaded"

        @allure.title("Check download file")
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "The file has not been download"

    @allure.feature("Dynamic Properties")
    class TestDynamicPropertiesPage:

        @allure.title("Check enable button")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "Button did not enable after 5 sec"

        @allure.title("Check dynamic properties")
        def test_dynamic_properties_page(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, "Colors has not been changed"

        @allure.title("Check appear_button")
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, "Button did not appear after 5 sec"
