#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 Nigus Tekleselassie Jimma, Ethiopia
# email nigustselassie@gmail.com
# -----------------------------------------------------------


#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
