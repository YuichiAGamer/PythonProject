# -*- coding: utf-8 -*-
import csv
import os
from Die import Die
from WeightedDie import WeightedDie

"""
In this script, makes die rolling result.
"""

# How many times tries to get die results.
attempts = 1000

# Defines row names.
# This is an example of application of list comprehensions.
# row_names_for_dice variables is to be declared as '["Die_1", "Die_2", "Die_3", "Die_4"]'.
# But this hard coding is a little redundant.
# Therefore declared as below.
row_names_for_dice = [("Die_" + str(number)) for number in range(0, 4)]


def try_die_rolling(die, attempts_number, die_name, applied_rows):
    roll_results = []

    # Rolls dies equal to attempts and records the results.
    for i in range(0, attempts_number):
        # die_1_result = die.roll()
        # die_2_result = die.roll()
        # Makes a dictionary whose keys are equal to applied_rows and gives values to each keys.
        roll_kv_pair = {}
        for each_die_name in applied_rows:
            roll_kv_pair.update({str(each_die_name): die.roll()})

        roll_results.append(roll_kv_pair)

    # Opens file in current directory of this script file.
    # "__file__" is a system variable which indicates the file name of executing script.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = die_name + "_" + str(attempts) + "_Attempts.csv"

    # Uses with statement. Reference to file is defined by keywords followed by "as".
    with open(current_directory + "\\" + file_name, "wt") as opened_file:
        # lineterminator variable should be declared explicitly as "\n".
        # Otherwise unintentional lines will be inserted.
        csv_out = csv.DictWriter(opened_file,
                                 fieldnames=applied_rows,
                                 lineterminator="\n")
        csv_out.writeheader()
        csv_out.writerows(roll_results)
        print("CSV writing done:" + opened_file.name)


# Prepares 3 dice.
normal_die = Die()
weighted_die_1 = WeightedDie(face=6, weights=[5, 1, 1, 1, 1, 1])
weighted_die_6 = WeightedDie(face=6, weights=[1, 1, 1, 1, 1, 5])

# With these 3 dice, obtains 3 results.
# Obtains 2d6.
try_die_rolling(normal_die, attempts,
                "double_normal_dice", [row_names_for_dice[1], row_names_for_dice[2]])
try_die_rolling(weighted_die_1, attempts,
                "double_1_weighted_dice", [row_names_for_dice[1], row_names_for_dice[2]])
try_die_rolling(weighted_die_6, attempts,
                "double_6_weighted_dice", [row_names_for_dice[1], row_names_for_dice[2]])

# Obtains 3d6.
try_die_rolling(normal_die, attempts,
                "triple_normal_dice", [row_names_for_dice[1], row_names_for_dice[2], row_names_for_dice[3]])
try_die_rolling(weighted_die_1, attempts,
                "triple_1_weighted_dice", [row_names_for_dice[1], row_names_for_dice[2], row_names_for_dice[3]])
try_die_rolling(weighted_die_6, attempts,
                "triple_6_weighted_dice", [row_names_for_dice[1], row_names_for_dice[2], row_names_for_dice[3]])
