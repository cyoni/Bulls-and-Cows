import random
import math

playing = False


def convertNumberToArray(numberToGuess):
    number_array = []
    for x in range(4):
        number_array.append(numberToGuess % 10)
        numberToGuess = math.floor(numberToGuess / 10)
    number_array.reverse()
    return number_array


def giveNumber():
    return random.randrange(1000, 9999, 1)


def printStatus(correct, wrong):
    print("bulls: ", correct, "cows: ", wrong)


def countCorrectAndWrongAnswer(input_array, number_array, correct, wrong):
    for i in range(4):
        if (input_array[i] == number_array[i]):
            correct += 1
        else:
            wrong += 1
    return [correct, wrong]


def startGame():
    global playing
    playing = True
    numberToGuess = giveNumber()
    print("ans ", numberToGuess)
    number_array = convertNumberToArray(numberToGuess)
    game(numberToGuess, number_array)


def game(numberToGuess, number_array):
    global playing
    while playing:
        user_input = input("Guess the number: ")
        input_array = convertNumberToArray(int(user_input))

        correct = 0
        wrong = 0

        status = countCorrectAndWrongAnswer(input_array, number_array, correct, wrong)
        correct = status[0]
        wrong = status[1]
        printStatus(correct, wrong)

        if (correct == 4):
            print("You win!")
            playing = False


startGame()
