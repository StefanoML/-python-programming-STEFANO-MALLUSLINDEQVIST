import math

x1, y1 = 4, 4
x2, y2 = 0, 1

k = (y2 - y1) / (x2 - x1)

#Now that we have k we can define m based on the formula y=kx+m

m = y1 -(k * x1)

print (f"'k' is {k} and 'm' is {m}." )
print (f"The equation for the slope is: y={k}x +{m}. ")

