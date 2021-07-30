# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
number = len(names)
#Write your code below this line 👇
person = names[random.randint(0, number - 1)]
print(f"{person} is paying the bill today!")



