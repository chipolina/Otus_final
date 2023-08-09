from selenium.webdriver.common.by import By

from tests.UI.page_objects.base_page import BasePage


class MainPage(BasePage):
    REGISTER = (By.CSS_SELECTOR, ".ico-register")
    LOGIN = (By.CSS_SELECTOR, ".ico-login")
    SHOPPINGCART = (By.CSS_SELECTOR, ".ico-cart")
    SHOPPINGCART_QTY = (By.CSS_SELECTOR, ".cart-qty")
    WL_QTY = (By.CSS_SELECTOR, ".wishlist-qty")
    BOOKS = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(@href,'/books')]")
    CATEGORIES = (
        By.XPATH, "//ul[@class='top-menu notmobile']//a[not(ancestor::ul[contains(@class, 'sublist first-level')])]")
    SEARCH_FIELD = (By.CSS_SELECTOR, '#small-searchterms')
    SEARCH_BTN = (By.XPATH, "//button[contains(@class,'search-box-button')]")

    def find_register_btn(self):
        return self.element(self.REGISTER)

    def find_login_btn(self):
        return self.element(self.LOGIN)

    def find_shopping_cart(self):
        return self.element(self.SHOPPINGCART)

    def find_shopping_cart_qty(self):
        return self.element(self.SHOPPINGCART_QTY)

    def find_books_btn(self):
        return self.element(self.BOOKS)

    def find_categories(self):
        return self.elements(self.CATEGORIES)

    def find_search_field(self):
        return self.element(self.SEARCH_FIELD)

    def find_search_btn(self):
        return self.element(self.SEARCH_BTN)
