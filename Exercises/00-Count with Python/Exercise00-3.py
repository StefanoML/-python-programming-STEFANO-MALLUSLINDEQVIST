import math

tp = 2
tn = 985
fp = 2
fn = 11

accuracy = ((tp + tn) / (tp + tn + fp + fn)*100)
print (f"The accuracy is {accuracy}%")
if (accuracy < 90):
    print("accuracy too low, this system is not accurate")
elif (accuracy > 100 or accuracy < 0):
    print("Incorrect value, please check the system.")
else: print("The system is accurate")