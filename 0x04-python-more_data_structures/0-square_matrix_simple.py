#!//usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''computes square value of all integers of a matrix'''
    return [[i**2 for i in row]for row in matrix]
