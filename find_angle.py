#solution for hackerrank's Find angle MBC problem

import math

side1=int(input())
side2=int(input())
angle=math.atan(side1/side2)
print(str(round(math.degrees(angle)))+"°")
