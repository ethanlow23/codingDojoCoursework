class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    
    def display_all(self):
        print 'price: ' + str(self.price) + '\nspeed: ' + self.speed + '\nfuel: ' + self.fuel + '\nmileage: ' + self.mileage + '\ntax: ' + str(self.tax)
        return self

car1 = Car(2000, '35mph', 'full', '15mpg')
car2 = Car(2000, '5mph', 'not full', '105mpg')
car3 = Car(2000, '15mph', 'kind of full', '95mph')
car4 = Car(2000, '25mph', 'full', '25mph')
car5 = Car(2000, '45mph', 'empty', '25mph')
car6 = Car(20000000, '35mph', 'empty', '15mph')