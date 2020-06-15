#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: tesuser 1, testuser 2, testuser 3

import random
import time
import sys

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("My randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


if __name__ == "__main__":
    outputfilename = "randomNumber"
    roll = get_random_number(1, 100)
    write_log_file(outputfilename, roll)
