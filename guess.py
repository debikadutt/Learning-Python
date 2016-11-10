import random

print("Hello, what is your favourite number?")
number = input()

print("your fav number is " + number)

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)
print(magicNumber)

message = "This program has a magic number between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("guess what it is?")
    guess = int(input())
    if guess == magicNumber:
        found = True
        print("****")
    if guess < magicNumber:
        print("Too low")
    if guess > magicNumber:
        print("Too high")
        
print ("you got it!")
