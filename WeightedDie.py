# -*- coding: utf-8 -*-

# This importing statement style is important
from Die import Die


class WeightedDie(Die):
    """
    Weighted die class inherited from Die class.
    When Face is created, The "weight" of each face can be set.
    The probability of which a named number can be obtained will be determined by an algorithm below:

    1. Gets sum of the weight of each number.
    e.g. Supposing there are 6 faces on this die
    and each face(1, 2, 3, 4, 5, 6) has these weight, relatively: 1, 1, 1, 2, 2, 4.
    Total "weight" is 1 + 1 + 1 + 2 + 2 + 4 = 11.

    2. Gets random number in range from 1 to "weight"(Each end point included).
    e.g. Supposing you get 7(In the range of 1 ~ 11).

    3. Sum up the weight of each faces of die, one by one, by ascending order.
    The sum should be less than the number obtained in step 2.
    e.g. The weight of face 1 is 1. add 1 to 0 and gets 1.
    Next face is 2, and weight is 1. add 1 to 1 and gets 2. and so on.

    4. If the sum of "weight" meets the number obtained in step 2 or exceeds it,
    Stop Summing up. Confirm current face and the face is rolled result.
    e.g. Until Adding the weight of face 4, sum of "weight" is 5, less than 7.
    After adding the "weight" of face 5, sum is 5 + 2 = 7, equal to the number obtained in step 2.
    Therefore stops summing up and 5 is the obtained face.

    """

    def __init__(self, face=6, weights=[]):
        self.face = 6
        self.face_Weights = {}

        i = 1
        for weight in weights:
            self.face_Weights.update({i: weights[i - 1]})
            i += 1

        print(self.face_Weights)


if __name__ == "__main__":
    first_weights = [1, 1, 1, 1, 1, 5]
    w_die = WeightedDie(6, first_weights)
