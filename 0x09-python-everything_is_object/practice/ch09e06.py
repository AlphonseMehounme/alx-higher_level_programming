"""
  ch09e06 module

  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
  >>> nlist[2][1]
  0
  >>> nlist[0][2]
  17
  >>> nlist[1][1]
  5
  >>> import string
  >>> message.split('??')
  ['this', 'and', 'that']
"""
a, b = 2, 7
junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
nlist = [[12, 13, 17], [14, 5], [1, 0]]
message = "this??and??that"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
