class ShoppingCart:
    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total += value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, item):
        self._items.append(item)

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, number):
        employee_discount = number

    def add_item(self, item, price, quantity = 1):
        new_item = dict(name = item, price = price, quantity = quantity)
        self._total += round((new_item['price']*new_item['quantity']), 2)
        self._items.append(new_item)


shopping_cart = ShoppingCart()
