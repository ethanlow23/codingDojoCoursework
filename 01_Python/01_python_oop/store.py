class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, productToAdd):
        self.products.append(productToAdd)
        return self

    def remove_product(self, productToRemove):
        self.products.remove(productToRemove)
        return self

    def inventory(self):
        for x in self.products:
            print x + ' is available for sale'
            return self

store1 = Store(['food', 'toys', 'clothes', 'alcohol'], 'bay area', 'bob')

store1.add_product('fish').remove_product('food').inventory()