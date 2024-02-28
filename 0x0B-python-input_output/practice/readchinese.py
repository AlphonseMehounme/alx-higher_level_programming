#!/usr/bin/python3
"""
  Read Chinese
"""


with open('chinese.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)

line_num = 0
with open('online.txt', encoding='utf-8') as fx:
    for line in fx:
        line_num += 1
        print('{:>4} {}'.format(line_num, line))
