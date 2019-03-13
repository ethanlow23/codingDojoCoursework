def problem1(arr)
    print arr.reduce(:+)
    return arr.find_all {|i| i > 10}
end
arr = [3,5,1,2,7,9,8,13,25,32]

def problem2(arr)
    print arr.shuffle
    return arr.find_all {|i| i.length > 5}
end
arr = ['John','KB','Oliver','Cory','Matthew','Christopher']

def shuffle_arr(arr)
    a = arr.shuffle
    print "first letter: ", a[0]
    print "last letter: ", a[a.length-1]
end
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def rand_num
    a = []
    (1..10).each do |i|
        a << rand(55..100)
    end
    a
end

def rand_num2
    a = []
    (1..10).each do |i|
        a << rand(55..100)
    end
    print a.sort, "\n"
    puts a.min
    puts a.max
    a
end

def rand_string
    (0...5).map{(65+rand(26)).chr}.join
end

def rand_string2
    a = []
    (1..10).each do |i|
        a << (0...5).map{(65+rand(26)).chr}.join
    end
    a
end