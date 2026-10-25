import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


class TestProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = (
            "http://selenium1py.pythonanywhere.com/catalogue/"
            "the-shellcoders-handbook_209/?promo=newYear"
        )

    @pytest.mark.parametrize(
        "promo",
        [
            "offer0",
            "offer1",
            "offer2",
            "offer3",
            "offer4",
            "offer5",
            "offer6",
            pytest.param("offer7", marks=pytest.mark.xfail),
            "offer8",
            "offer9",
        ],
    )
    def test_guest_can_add_product_to_basket(self, browser, promo):
        link = (
            "http://selenium1py.pythonanywhere.com/catalogue/"
            f"coders-at-work_207/?promo={promo}"
        )
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_added_to_basket()
        page.should_be_basket_total_equal_product_price()

    @pytest.mark.xfail(reason="Success message is expected after adding a product")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(
        self, browser
    ):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Success message does not disappear automatically")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message_after_disappeared()


class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = (
            "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
            "the-city-and-the-stars_95/"
        )

    @pytest.mark.login_guest
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.login_guest
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()


class TestBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = (
            "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
            "the-city-and-the-stars_95/"
        )

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_have_products()
        basket_page.should_be_empty()
