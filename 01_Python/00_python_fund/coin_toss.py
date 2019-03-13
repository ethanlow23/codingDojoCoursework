import random
def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        rand_num = random.random()
        if round(rand_num) == 0:
            heads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(heads) + "head(s) so far and " + str(tails) + " tail(s) so far"
        elif round(rand_num) == 1:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + "head(s) so far and " + str(tails) + " tail(s) so far"
