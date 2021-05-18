import random
import time
import sys

print("This is a 2 player game of snake and ladder")

pos1 = 0
pos2 = 0


def check(pos):
    ladder = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    snake = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 48: 26, 16: 6}
    for key in ladder:
        if key == pos:
            print("Woah! You has found the ladder")
            pos = ladder[pos]
            return pos
    for key in snake:
        if key == pos:
            print("Sorry, You are bitten by a snake")
            pos = snake[pos]
            return pos
    return pos


def roll(pos):
    time.sleep(1)
    print("Now is your chance to roll the die")
    die_num = random.randint(1,6)
    print("It has come out to be {}".format(die_num))
    if pos + die_num <= 100:
        pos += die_num
    return pos


def player_names():
    print("Please provide the name of the 1st player")
    name1 = str(input())
    print("Please provide the name of the 2nd player")
    name2 = str(input())
    print("So, this match is between {} and {}".format(name1, name2))
    return name1, name2


player1_name, player2_name = player_names()


while pos1 < 100 and pos2 < 100:

    print("Now its your turn {}".format(player1_name))
    pos1 = roll(pos1)
    pos1 = check(pos1)
    print("So, after this turn the positions are:")
    print("{} - {}".format(player1_name, pos1))
    print("{} - {}".format(player2_name, pos2))

    if pos1 == 100:
        print("The Winner of the game is {}".format(player1_name))
        break

    print("Now its your turn {}".format(player2_name))
    pos2 = roll(pos2)
    pos2 = check(pos2)
    print("So, after this turn the positions are:")
    print("{} - {}".format(player1_name, pos1))
    print("{} - {}".format(player2_name, pos2))

    if pos2 == 100:
        print("The Winner of the game is {}".format(player2_name))
        break


print("Hope you enjoyed the game {} and {}!".format(player2_name, player1_name))




