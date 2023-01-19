import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "[]{}\|:;<,>.?/_-+=!@#$%^&*()"

all = lower + upper + numbers +symbols
print("Password Generator")
print("@mmatej16 on Github")
length = int(input('\nEnter the length of the password(s): '))
num = int(input('\nEnter how many passwords you want to generate?: '))
print("")
print("Your generated password(s) are:")
print("")
for n in range (0, num):
    password = "".join(random.sample(all,length))
    print(password)
