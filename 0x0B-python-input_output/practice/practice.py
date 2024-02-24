"""
  Practice Module
"""


with open('iamafile.txt') as f:
    """cont = f.read()
    print(cont)
    print('-----')
    content = f.read(5)
    print(content)
    print('-----')
    line1 = f.readline()
    print(line1)
    print('-----')"""
    for line in f.readlines():
        print(line)
