#!/usr/bin/python3
"""
  Write and Read Module
"""


with open('test.log', mode='w', encoding='utf-8') as f:
    f.write('test succeeded')
with open('test.log', mode='r', encoding='utf-8') as f:
    content = f.read()
    print(content)
with open('test.log', mode='a', encoding='utf-8') as f:
    f.write(content)
with open('test.log', encoding='utf-8') as f:
    print(f.read())
