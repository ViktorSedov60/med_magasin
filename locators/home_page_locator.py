from selenium.webdriver.common.by import By


class HeaderMenuLocator:
    LOGO = (By.CSS_SELECTOR, 'div.align-middle .logo a img')
    HEADER_MENU = (By.CSS_SELECTOR, 'ul.menu.main li a')
    SELECT_CITY = (By.CSS_SELECTOR, 'div.align-middle div.city span.name')
    ITEM_CITY = (By.CSS_SELECTOR, 'div.align-middle li.selectOption')



class MenuTestLocator:
    CATALOG_MENU = (By.CSS_SELECTOR, 'div.catalogue-menu')
    MENU_ITEM_LIST = (By.CSS_SELECTOR, '.catalogue-menu-mobile ul li.menu-item.expanded a')
    SEARCH_INPUT = (By.CSS_SELECTOR, '')
    FULL_MENU = (By.CSS_SELECTOR, 'div.left-menu ul li a')

8394738