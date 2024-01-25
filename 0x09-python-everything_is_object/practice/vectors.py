"""
  Vector Module

"""


def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
    if type(u) != list or type(v) != list:
        raise TypeError("u and v must be lists")
    if len(u) != len(v):
        raise TypeError("u and v must me of the same lenght")
    newl = [0] * len(u)
    for i in range(len(u)):
        newl[i] = u[i] + v[i]
    return newl

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    for i in range(len(v)):
        v[i] *= s
    return v

def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    sum = 0
    for i in range(len(u)):
        sum += u[i] * v[i]
    return sum


#print(add_vectors([1, 0], [1, 1]))
