# -*- coding: utf-8 -*-
import random


class Die:
    """
    A class of 1 die. The number of face can be any number, default is 6.
    """
    def __init__(self, face=6):
        """
        Makes this instance.
        :param face: The number of face of this die. default is 6.
        """
        self.face = face

    def roll(self):
        return random.randint(1, self.face)


if __name__ == "__main__":
    print("This will be a Die class.")
    die = Die()
    print("The result was {}".format(die.roll()))
