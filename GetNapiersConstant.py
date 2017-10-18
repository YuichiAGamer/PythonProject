# -*- coding: utf-8 -*-

"""
Calculates Napier's constant by the definition of e = lim(x->infinity)(1 + 1 / x)^x
"""

x = 1
x_max = 1000

for i in range(x, x_max + 1):
    e = pow((1 + 1 / i), i)
    print("e is {} when x = {}".format(e, i))

