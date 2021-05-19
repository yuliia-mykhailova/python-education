"""Module main for testing"""

from customer import Customer
from product import Product
from restaurant import Restaurant
from dish import Dish
from disease import Disease
from waiter import Waiter


if __name__ == '__main__':
    restaurant = Restaurant('Test', 'address')
    print(restaurant)

    orange = Product('Orange')
    strawberry = Product('Strawberry')
    chocolate = Product('Chocolate')
    lemon = Product('Lemon')
    milk = Product('Milk')
    egg = Product('Egg')
    tomato = Product('Tomato')
    cucumber = Product('Cucumber')
    print(orange)

    dish1 = Dish('Dish1', [orange, chocolate, milk], 34.5, 10)
    dish2 = Dish('Dish2', [lemon, strawberry, orange], 23, 5)
    dish3 = Dish('Dish3', [egg, milk, chocolate], 50, 8)
    dish4 = Dish('Dish4', [tomato, cucumber, orange], 30, 7)
    print(dish1)

    restaurant.menu = [dish1, dish2, dish3, dish4]
    for dish in restaurant.menu:
        print(dish)

    disease1 = Disease('Citrus allergy', [orange, lemon])
    disease2 = Disease('Strawberry allergy', [strawberry])
    disease3 = Disease('Lactose intolerance', [milk, egg])
    disease4 = Disease('Chocolate allergy', [chocolate])
    print(disease1)

    customer = Customer('Robert', 'Smith', 'robert.smith@gmail.com', [disease4])
    print(customer)

    menu_customer = customer.get_personal_menu(restaurant)
    for dish in menu_customer:
        print(dish)

    waiter = Waiter('Elliot', 'Smith', 35.7)
    print(waiter)

    order1 = waiter.take_order(customer, [dish2, dish4])
    print(order1)

    print(order1.get_full_price())

    waiter.bring_order(order1)
    order1.pay_for_order(60)

    print(waiter.get_salary())

    restaurant.waiters = [waiter]
    restaurant.orders = [order1]

    for order in restaurant.orders:
        print(order)
    for waiter in restaurant.waiters:
        print(waiter)
