#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Stefani Diaz, Lakshay Khurana, Panda
# expert of exercise block 1: Stefani Diaz

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename+".log", "a")
    f.write("Our randomly generated color is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice(spots):
    colors = ["blue", "green", 'red', 'yellow', 'purple', 'orange']
    return colors[spots-1]


def get_color_by_dice_naive(spots):
    if spots == 1:
        color = 'blue'
    elif spots == 2:
        color = 'green'
    elif spots == 3:
        color = 'red'
    elif spots == 4:
        color = 'yellow'
    elif spots == 5:
        color = 'purple'
    else: # spots == 6:
        color = 'orange'
    return color


if __name__ == "__main__":
    outputfilename = "randomNumber"
    roll = get_random_number(1, 6)
    color = get_color_by_dice(roll)
    write_log_file(outputfilename, color)
    rolls=[]
    for i in range(6):
        roll = get_random_number(1, 6)
        rolls.append(roll)
    print(rolls)
    sys.stdout.flush()
    plt.barh(range(6),rolls)
    plt.show()