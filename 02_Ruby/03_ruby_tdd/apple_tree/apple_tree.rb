class AppleTree
    attr_accessor :age
    attr_reader :height, :apple_count
    def initialize(age)
        @age = age
        @height = 10
        @apple_count = 5
    end
    def year_gone_by
        @age += 1
        @height *= 1.1
        @apple_count += 2
        "age: #{@age}, height: #{@height}, count: #{@apple_count}"
    end
    def pick_apples
        @apple_count = 0
    end
end