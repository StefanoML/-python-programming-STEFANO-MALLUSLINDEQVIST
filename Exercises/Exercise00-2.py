import math

#I made a generic version to take any input instead of having constants
predictions=float (input(f"Input amount of predictions"))
correct=float (input(f"input amount of correct predictions"))
accuracy=round((correct / predictions)*100, 2)
print (accuracy)