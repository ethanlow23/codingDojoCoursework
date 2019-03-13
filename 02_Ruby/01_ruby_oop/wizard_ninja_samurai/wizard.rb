class Wizard < Human
    attr_accessor :health, :intelligence
    def initialize
        super()
        @health = 50
        @intelligence = 25
    end
    def heal
        @health += 10
        self
    end
    def fireball(object)
        object.health -= 20
        self
    end
end