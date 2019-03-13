class Samurai < Human
    @@samurai_count = 0
    attr_accessor :health
    def initialize
        super()
        @health = 200
        @@samurai_count += 1
    end
    def death_blow(object)
        object.health = 0
        self
    end
    def meditate
        @health = 200
        self
    end
    def self.how_many
        @@samurai_count
    end
end