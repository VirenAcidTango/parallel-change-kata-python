from field import ShoppingCart
from method import AuthenticationService


def test_administrator_is_always_authenticated():
    service = AuthenticationService()
    adminId = 12345
    assert service.is_authenticated(adminId)


def test_normal_user_is_not_authenticated_initially():
    service = AuthenticationService()
    normalUserId = 11111
    assert not service.is_authenticated(normalUserId)


def test_cat_may_just_have_a_single_item():
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    assert 1 == shoppingCart.number_of_products()


def test_the_total_price_of_the_cart_is_total_of_its_contents():
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    assert 10 == shoppingCart.calculate_total_price()


def test_has_discount_when_contains_at_least_one_premium_item():
    shoppingCart = ShoppingCart()
    shoppingCart.add(100)
    assert shoppingCart.has_discount()


def test_doesnt_have_discount_when_all_its_items_are_cheap():
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    assert not shoppingCart.has_discount()
