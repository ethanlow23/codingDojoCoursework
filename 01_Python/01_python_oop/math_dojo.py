'''
# Part I
class MathDojo(object):
    def __init__(self):
        self.total = 0
        
    def add(self, add_num, *add_nums):
        for i in add_nums:
            add_num += i
        self.total += add_num
        return self
  
    def subtract(self, sub_num, *sub_nums):
        for i in sub_nums:
            sub_num += i
        self.total -= sub_num
        return self
  
  def result(self):
    print self.total
    return self
    
md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

# Part II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter 
with any number of values passed into the list. It should now be able to perform the following tasks:
'''
class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, add_num, *add_nums):
        if isinstance(add_num, list):
            for x in add_num:
                self.total += x
            for i in add_nums:
                if isinstance(i, list):
                    for j in i:
                        self.total += j
                elif isinstance(i, int):
                    self.total += i
        elif isinstance(add_num, int):
            for i in add_nums:
                if isinstance(i, list):
                    for j in i:
                        add_num += j
                elif isinstance(i, int):
                    add_num += i
            self.total += add_num
        return self
  
    def subtract(self, sub_num, *sub_nums):
        if isinstance(sub_num, list):
            sum = 0
            for i in sub_num:
                sum += i
            for i in sub_nums:
                if isinstance(i, list):
                    for j in i:
                        sum += j
                elif isinstance(i, int):
                    sum += i
            self.total -= sum
        elif isinstance(sub_num, int):
            for i in sub_nums:
                if isinstance(i, list):
                    for j in i:
                        sub_num += j
                elif isinstance(i, int):
                    sub_sum += i
            self.total -= sub_num
        return self
  
    def result(self):
        print self.total
        return self

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
# 27.15

# Part III
# Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.