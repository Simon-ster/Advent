f = open("textdata.txt", "r")
total = 0
'''
def test(x):
    for y in numb:
        if x % y == 0:
            if x != y:
                return x/y
    return 0
'''

for line in f:
    j = line.split()
    numb = []
    for z in j:
        numb.append(int(z))
    
    for x in numb:
        for y in numb:
            if x % y == 0:
                if x != y:
                    total += x/y

print total

