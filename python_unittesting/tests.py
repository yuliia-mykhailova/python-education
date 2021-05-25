import pytest
from unittest import mock

from python_unittesting.software_to_test.to_test import *


# even_odd()
@pytest.mark.parametrize('test_arg, expected',
                         [(1, 'odd'),
                          (10, 'even'),
                          (-4, 'even'),
                          (1.0, 'odd')])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_even_odd_none_arg_test():
    test_arg = None
    with pytest.raises(TypeError):
        even_odd(test_arg)


def test_even_odd_string_arg_test():
    test_arg = 'qwerty'
    with pytest.raises(TypeError):
        even_odd(test_arg)


# sum_all()
@pytest.mark.parametrize('test_arg, expected',
                         [(1, 1),
                          (2.2, 2.2)])
def test_sum_all_one_number(test_arg, expected):
    assert sum_all(test_arg) == expected


@pytest.mark.parametrize('test_arg, expected',
                         [((1, 2, 3, 4, 5), 15),
                          ((2.2, 2.2, 2.5, 0.1, 0.05), 7.05),
                          ((0, -5, 5), 0)])
def test_sum_all_list(test_arg, expected):
    assert sum_all(*test_arg) == expected


def test_sum_string_arg():
    test_arg = ['qwerty', 'abcd']
    with pytest.raises(TypeError):
        sum_all(*test_arg)


def test_sum_none_arg():
    test_arg = None
    with pytest.raises(TypeError):
        sum_all(test_arg)


# time_of_day()
@pytest.mark.parametrize('test_arg, expected',
                         [([2021, 5, 25, 8, 0, 0], 'morning'),
                          ([2021, 5, 25, 3, 0, 0], 'night'),
                          ([2021, 5, 25, 12, 0, 0], 'afternoon'),
                          ([2021, 5, 25, 22, 0, 0], 'night')])
@mock.patch('python_unittesting.software_to_test.to_test.datetime')
def test_time_of_day(mocked_datetime, test_arg, expected):
    mocked_datetime.now.return_value = datetime(*test_arg)
    assert time_of_day() == expected


# product
@pytest.fixture()
def negative_quantity_product():
    """Returns a Product instance with negative quantity"""
    return Product('negative', 20, -3)


@pytest.fixture()
def zero_quantity_product():
    """Returns a zero quantity Product"""
    return Product('zero', 10, 0)


@pytest.fixture()
def normal_product():
    """Returns a normal Product"""
    return Product('normal', 10, 4)


# subtract_quantity
def test_subtract_quantity_normal(normal_product):
    normal_product.subtract_quantity(0)
    assert normal_product.quantity == 4
    normal_product.subtract_quantity(2)
    assert normal_product.quantity == 2
    normal_product.subtract_quantity()
    assert normal_product.quantity == 1


def test_subtract_quantity_to_negative(normal_product):
    normal_product.subtract_quantity(7)
    assert normal_product.quantity == -3


# add_quantity
def test_add_quantity_normal(normal_product):
    normal_product.add_quantity(100)
    assert normal_product.quantity == 104
    normal_product.add_quantity()
    assert normal_product.quantity == 105


def test_add_quantity_from_negative(negative_quantity_product):
    negative_quantity_product.add_quantity(0)
    assert negative_quantity_product.quantity == -3
    negative_quantity_product.add_quantity(2)
    assert negative_quantity_product.quantity == -1
    negative_quantity_product.add_quantity(11)
    assert negative_quantity_product.quantity == 10


# change_price
def test_change_price_to_negative(normal_product):
    normal_product.change_price(-10)
    assert normal_product.price == -10


def test_change_price_to_very_small(normal_product):
    normal_product.change_price(0.000008)
    assert normal_product.price == 0.000008


# shop
@pytest.fixture
def empty_shop():
    """Returns empty list of products"""
    return Shop()


@pytest.fixture
def shop_with_one_zero_quantity_product(zero_quantity_product):
    """Returns a Shop with zero quantity product"""
    return Shop(zero_quantity_product)


@pytest.fixture
def shop_with_one_negative_quantity_product(negative_quantity_product):
    """Returns a Shop with negative quantity product"""
    return Shop(negative_quantity_product)


@pytest.fixture
def shop_with_three_different_products(normal_product, negative_quantity_product, zero_quantity_product):
    """Returns a Shop list of products"""
    return Shop([normal_product, negative_quantity_product, zero_quantity_product])


# add_product
def test_shop_add_product(empty_shop, normal_product, zero_quantity_product):
    assert empty_shop.products == []
    empty_shop.add_product(normal_product)
    assert empty_shop.products == [normal_product]
    empty_shop.add_product(zero_quantity_product)
    assert empty_shop.products == [normal_product, zero_quantity_product]
    assert empty_shop.products[0].title == 'normal'
    assert empty_shop.products[1].quantity == 0


# _get_product_index
def test_shop_get_product_index(shop_with_three_different_products):
    assert shop_with_three_different_products._get_product_index('normal') == 0
    assert shop_with_three_different_products._get_product_index('negative') == 1
    assert shop_with_three_different_products._get_product_index('zero') == 2
    assert shop_with_three_different_products._get_product_index('smth') is None
    with pytest.raises(TypeError):
        shop_with_three_different_products._get_product_index()


# sell_product
def test_shop_sell_product_normal(shop_with_three_different_products):
    assert shop_with_three_different_products.sell_product('normal') == 10
    assert shop_with_three_different_products.products[0].quantity == 3
    shop_with_three_different_products.sell_product('normal', 3)
    assert shop_with_three_different_products._get_product_index('normal') is None
    assert shop_with_three_different_products.money == 40


def test_shop_sell_product_zero_none(shop_with_three_different_products):
    with pytest.raises(ValueError):
        shop_with_three_different_products.sell_product('normal', 10)
    with pytest.raises(TypeError):
        shop_with_three_different_products.sell_product()
    with pytest.raises(ValueError):
        shop_with_three_different_products.sell_product('zero')


def test_shop_sell_negative(shop_with_three_different_products):
    shop_with_three_different_products.sell_product('normal', -10)
    assert shop_with_three_different_products.products[0].quantity == 14
