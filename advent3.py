numb = 312051
x = 1
y = 0

while (x)*(x) < numb:
    x += 2
    y = x*x

    
print str(x) + ", " + str(y)
halfway = ((x / 2))
print halfway

sideSubtract = abs(1 - x)
print sideSubtract
    
if y - sideSubtract < numb:
    mid = y - halfway
elif y - (2 * sideSubtract) < numb:
    mid = (y - sideSubtract) - halfway
elif y - (3 * sideSubtract) < numb:
    mid = (y - (2 * sideSubtract)) - halfway
elif y - (4 * sideSubtract) < numb:
    mid = (y - (3 * sideSubtract)) - halfway

print mid

distSide = abs(numb - mid)
distance = halfway + distSide
print distance

