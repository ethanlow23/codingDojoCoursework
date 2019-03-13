class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'price: ' + str(self.price)
        print 'max speed: ' + self.max_speed
        print 'miles traveled: ' + str(self.miles)
        return self
    
    def ride(self):
        print 'riding'
        self.miles += 10
        return self

    def reverse(self):
        print 'reversing'
        self.miles -= 5
        return self

bike1 = Bike(200, '25 mph')
bike2 = Bike(200, '25 mph')
bike3 = Bike(200, '25 mph')

print 'bike one'
bike1.ride().ride().ride().reverse().displayInfo()
print 'bike two'
bike2.ride().ride().reverse().reverse().displayInfo()
print 'bike three'
bike3.reverse().reverse().reverse().displayInfo()