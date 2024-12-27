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


def test_cat_may_just_have_a_single_item():
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
