#  Add your doctests here:
"""
  Test Driven Development practice

  >>> range = ranges
  >>> a_list[3]
  42
  >>> a_list[6]
  'Ni!'
  >>> len(a_list)
  8
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
  >>> 'war' in mystery_list
  False
  >>> 'peace' in mystery_list
  True
  >>> 'justice' in mystery_list
  True
  >>> 'oppression' in mystery_list
  False
  >>> 'equality' in mystery_list
  True
  >>> range(a, b, c)
  [5, 9, 13, 17]
"""
# Write your Python code here:

a_list = [1, 2, 3, 42, 6, 7, 'Ni!', 'Al']
b_list = ['I', 'Stills', 'Nash']
c_list = ['Young']
mystery_list = ['peace', 'justice', 'equality']
a = 5
b = 18
c = 4

def ranges(a, b, c):
    ls = []
    for i in range(a, b, c):
        ls += [i]
    return ls

if __name__ == '__main__':
    import doctest
    doctest.testmod()
