# -*- coding: utf-8 -*-

# This importing statement style is important
from Die import Die
import random


class WeightedDie(Die):
    """
    Weighted die class inherited from Die class.
    When Face is created, The "weight" of each face can be set.
    The probability of which a named number can be obtained will be determined by an algorithm below.
    Suppose this algorithm is called "Cumulative Weight Search"(CMS). :

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
        self.face_weights = {}

        # Repeats equal to the value of face
        for i in range(1, (face + 1)):
            # If there is a weight setting for target face, use that.
            # If there is not, weight of target face is assumed as 1.
            if len(weights) >= i:
                self.face_weights.update({i: weights[i - 1]})
            else:
                self.face_weights.update({i: 1})

    def roll(self):
        """
        Overrides super class method.
        Returns the value of face which is determined by Cumulative Weight Search.
        :return: Value of face affected by the weight of each faces.
        """

        # Gets the random number between 1 to sum-of-weight.
        obtained_weight = random.randint(1, self._get_total_weight())

        # Get sorted faces of this die.
        sorted_faces = self._get_sorted_faces()

        # Sum up weight by this variable
        weight_sum = 0

        for sorted_face in sorted_faces:

            weight_sum += self.face_weights[sorted_face]
            if weight_sum >= obtained_weight:
                return sorted_face

        return None  # Returns none if process reaches here, to indicate unexpected result.

    def _get_total_weight(self):
        """
        Returns total weight of this die.
        This method is not needed by outer class, therefore underscore("_") is used.
        :return: total weight of this die
        """
        total_weight = 0
        die_weights = self.face_weights.values()

        for die_weight in die_weights:
            total_weight += die_weight

        return total_weight

    def _get_sorted_faces(self):
        """
        Returns an array of faces on this die as ascending order.
        :return: An array of faces on this die as ascending order.
        """
        sorted_faces = sorted(self.face_weights.keys())
        return sorted_faces


if __name__ == "__main__":
    first_weights = [5, 1, 1, 1, 1, 1]
    w_die = WeightedDie(6, first_weights)
    print(w_die.face_weights)
    print(w_die._get_total_weight())

    print("Tries rolling this die.")
    for attempt in range(1, 11):
        print("Attempt {}: result is {}".format(attempt, w_die.roll()))

