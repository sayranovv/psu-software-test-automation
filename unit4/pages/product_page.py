from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_be_product_added_to_basket(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        added_product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_TO_BASKET
        ).text
        assert product_name == added_product_name, (
            "Product name in the basket message does not match the product"
        )

    def should_be_basket_total_equal_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text
        assert product_price == basket_total, (
            "Basket total does not match the product price"
        )
