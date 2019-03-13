class Ninja < Human
    attr_accessor :stealth
    def initialize
        super()
        @stealth = 175
    end
    def steal(object)
        @health += 10
        self
    end
    def get_away
        @health -= 15
        self
    end
end