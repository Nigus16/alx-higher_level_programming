#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to compute the square value of all integers of a matrix
# using map
#
# (C) 2023 Nigus Tekleselassie Jimma, Ethiopia
# email nigustselassie@gmail.com
# -----------------------------------------------------------


#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
