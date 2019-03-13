class Human
    attr_accessor :strength, :stealth, :intelligence, :health
    def initialize
        @strength = 3
        @stealth = 3
        @intelligence = 3
        @health = 100
    end
    def attack(object)
        if object.class.ancestors.include?(Human)
            object.health -= 1
            true
        else
            false
        end
    end
end