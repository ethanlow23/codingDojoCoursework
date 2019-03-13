class MathDojo
    def initialize
        @result = 0
    end
    def add *nums
        for num in nums
            if num.class == Array
                num.each {|i| @result += i}
            else
                @result += num
            end
        end
        self
    end
    def subtract *nums
        @total = 0
        for num in nums
            if num.class == Array
                num.each {|i| @total += i}
            else
                @total += num
            end
        end
        @result -= @total
        self
    end
    def result
        puts @result
        self
    end
end

challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).result # => 4
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).result # => 23.15