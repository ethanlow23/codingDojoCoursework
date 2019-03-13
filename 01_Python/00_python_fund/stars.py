# stars: part I
def draw_stars(lst):
    for i in lst:
        print '*' * i

# stars: part II
def draw_stars(x):
    for i in x:
        if isinstance(i, int):
            print '*' * i
        else:
            print i[0].lower() * len(i)