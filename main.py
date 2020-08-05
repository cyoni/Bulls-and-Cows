import random

playing = True

number = random.randrange(1000, 9999, 1)


success = []

for x in range(4):
    success.append("*")

while playing:
    print("Guess the number ", success)
    user_input = input("Guess the number: ")
    print("hi " + user_input)
