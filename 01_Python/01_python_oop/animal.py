class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health += 5
        return self

    def display_health(self):
        print 'Animals health: ' + str(self.health)
        return self

# animal1 = Animal('animal', 100)
# animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog('dawg')
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__()
        self.health = 170

    def fly(self):
        self.health += 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print 'i am a dragon'