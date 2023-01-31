from pages.interaction_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteraction:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no elements were selected"
            assert len(item_grid) > 0, "no elements were selected"

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizable has not been changed"

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', "The div has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            drop_text_not_accept, drop_text_accept = droppable_page.drop_accept()
            assert drop_text_not_accept == 'Drop here', "The div has been accepted"
            assert drop_text_accept == 'Dropped!', "The div has not been accepted"

        def test_prevent_propogation(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box = droppable_page.drop_prevent_propogation()
            assert text_not_greedy_box == 'Dropped!', "the elements texts has not been changed"
            assert text_not_greedy_inner_box == 'Dropped!', "the elements texts has not been changed"
            assert text_greedy_box == 'Outer droppable', "the elements texts has been changed"
            assert text_greedy_inner_box == 'Dropped!', "the elements texts has not been changed"

        def test_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            before_will, after_will = droppable_page.drop_will_revert_draggable()
            assert before_will != after_will, "Coordinates has not been changed"
            before_not, after_not = droppable_page.drop_not_revert_draggable()
            assert before_not == after_not, "Coordinates has been changed"

