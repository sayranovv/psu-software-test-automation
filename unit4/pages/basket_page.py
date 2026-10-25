from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_have_products(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Products are presented in the basket"

    def should_be_empty(self):
        empty_basket_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET
        ).text
        assert "Your basket is empty." in empty_basket_message, (
            "Empty basket message is not presented"
        )
