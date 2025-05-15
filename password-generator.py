import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&amp:*"
length = int(input("Enter the password length: "))
password = ""
for i in range(length+1):
    password += random.choice(characters)
print("password is: ", password)
