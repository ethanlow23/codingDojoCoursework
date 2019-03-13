class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        self.price *= (1.0 + tax)
        return self

    def returned(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'opened':
            self.status = 'used'
            self.price *= 0.8
        return self

    def display_info(self):
        print 'price: ' + str(self.price)
        print 'item_name: ' + self.item_name
        print 'weight: ' + str(self.weight)
        print 'brand: ' + self.brand
        print 'status: ' + self.status
        return self

product1 = Product(50, 'product', 100, 'brand')

product1.sell().add_tax(0.1).returned('defective').display_info()