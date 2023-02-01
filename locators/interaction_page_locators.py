from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    ITEM_GRID = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (
        By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR,
                            'div[class="constraint-area"] span[class="react-resizable-handle '
                            'react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR,
                        'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.XPATH, '//div[@id="resizable"]')


class DroppablePagLocators:
    # Simple
    SIMPLE_TAB = (By.XPATH, '//a[@id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.XPATH, '//div[@id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[id="droppable"]')  # можно заменить на
    # запись '#simpleDropContainer #droppable'

    # Accept
    ACCEPT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.XPATH, '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = (By.XPATH, '//div[@id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propogation
    PREVENT_PROPOGATION_TAB = (By.XPATH, '//a[@id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT = (By.XPATH, '//div[@id="dragBox"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREDDY_INNER_DROPPABLE = (By.CSS_SELECTOR, '#notGreedyInnerDropBox')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREDDY_INNER_DROPPABLE = (By.CSS_SELECTOR, '#greedyDropBoxInner')

    # Revert_Draggable
    REVERT_DRAGGABLE_TAB = (By.XPATH, '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:
    # Simple
    SIMPLE_TAB_DRAGGABLE = (By.XPATH, '//a[@id="draggableExample-tab-simple"]')
    DRAG_ME_SIMPLE_DRAGGABLE = (By.CSS_SELECTOR, '#dragBox')

    # Axis Restricted
    AXIS_RESTRICTED_TAB = (By.XPATH, '//a[@id="draggableExample-tab-axisRestriction"]')
    ONLY_X_AXIS_RESTRICTED = (By.XPATH, '//div[@id="restrictedX"]')
    ONLY_Y_AXIS_RESTRICTED = (By.XPATH, '//div[@id="restrictedY"]')

    # Container Restricted
    CONTAINER_RESTRICTED_TAB = (By.XPATH, '//a[@id="draggableExample-tab-containerRestriction"]')

    # Cursor style
    CURSOR_STILE_TAB = (By.XPATH, '//a[@id="draggableExample-tab-cursorStyle"]')
