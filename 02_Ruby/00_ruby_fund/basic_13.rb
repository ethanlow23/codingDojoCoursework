# PRINT 1-255
(1..255).find_all{|i| puts i}

# PRINT ODD NUMBERS BETWEEN 1-255
(1..255).find_all{|i| puts i if i % 2 == 1}

# PRINT SUM
sum = 0
for i in 0...256
    sum += i
    puts "new number: " + i.to_s + " sum: " + sum.to_s
end

# ITERATING THROUGH AN ARRAY
[1,3,5,7,9,13].find_all{|i| puts i}

# FIND MAX
[-3,-5,-7,0,4,7].max

# GET AVREAGE
x = [2,10,3]
x.reduce(:+) / x.length

# ARRAY WITH ODD NUMBERS
y = []
(1..255).find_all{|i| y >> i if i % 2 != 0}

# GREATER THAN Y
def greater_than_y(arr, y)
    count = 0
    for i in arr
        if i > y
            count += 1
        end
    end
end
# SQUARE THE VALUES
def square_the_values(arr)
    for i in 0...arr.length
        arr[i] *= arr[i]
    end
end
# ELIMINATE NEGATIVE NUMBERS
def eliminate_negatives(arr)
    for i in 0...arr.length
        if arr[i] < 0
            arr[i] = 0
        end
    end
    return arr
end
# MAX, MIN, AND AVERAGE
def max_min_avg(arr)
    hash = {'max': arr.max, 'min': arr.min}
    sum = 0
    for i in arr
        sum += i
    end
    hash['avg'] = sum / arr.length
    return hash
end
# SHIFTING THE VALUES IN THE ARRAY
def shift_values(arr)
    for i in 0...arr.length-1
        arr[i] = arr[i + 1]
    end
    arr[arr.length - 1] = 0
    return arr
end
# NUMBER TO STRING
def num_to_string(arr)
    for i in 0...arr.length
        if arr[i] < 0
            arr[i] = 'Dojo'
        end
    end
    return arr
end