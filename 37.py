import math
x, y = 10, 20
r = 30
x1 = int(input("Enter x-coordinate: "))
y1 = int(input("Enter y-coordinate: "))
distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
if distance < r:
    print("inside")
elif distance > r:
    print("outside")
else:
    print("on")
