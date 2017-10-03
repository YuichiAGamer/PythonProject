# -*- coding: utf-8 -*-
import random


class Die:
    def __init__(self):
        self.face = 6

    def roll(self):
        return random.randint(1, self.face)


if __name__ == "__main__":
    print("This will be a Die class.")
    die = Die()
    print("The result was {}".format(die.roll()))
