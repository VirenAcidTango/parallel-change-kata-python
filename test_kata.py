from field import ShoppingCart
from method import AuthenticationService


def test_administrator_is_always_authenticated():
    service = AuthenticationService()
    admin_id = 12345
    assert service.is_authenticated(admin_id)


def test_normal_user_is_not_authenticated_initially():
    service = AuthenticationService()
    normal_user_id = 11111
    assert not service.is_authenticated(normal_user_id)


def test_cart_may_just_have_a_single_item():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    assert 1 == shopping_cart.number_of_products()


def test_the_total_price_of_the_cart_is_total_of_its_contents():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    assert 10 == shopping_cart.calculate_total_price()


def test_has_discount_when_contains_at_least_one_premium_item():
    shopping_cart = ShoppingCart()
    shopping_cart.add(100)
    assert shopping_cart.has_discount()


def test_doesnt_have_discount_when_all_its_items_are_cheap():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    assert not shopping_cart.has_discount()

def test_calculates_total_many_items():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    shopping_cart.add(10)
    assert shopping_cart.calculate_total_price() == 20

def test_calculates_discount_many_items():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    shopping_cart.add(85)
    shopping_cart.add(135)
    shopping_cart.add(94)
    assert shopping_cart.has_discount()

def test_cart_has_many_items():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    shopping_cart.add(10)
    shopping_cart.add(10)
    assert shopping_cart.number_of_products() == 3

def test_cart_adds_many_items_at_once():
    shopping_cart = ShoppingCart()
    shopping_cart.add(10, 20, 30)
    assert shopping_cart.number_of_products() == 3