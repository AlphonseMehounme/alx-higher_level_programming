#!/usr/bin/python3
"""
  Write and Read Module
"""
import os


with open('test.log', mode='w', encoding='utf-8') as f:
    f.write('test succeeded')
with open('test.log', mode='r', encoding='utf-8') as f:
    content = f.read()
    print(content)
with open('test.log', mode='a', encoding='utf-8') as f:
    f.write(content)
with open('test.log', encoding='utf-8') as f:
    print(f.read())
os.rename('test.log', 'newtest.log')
with open('newtest.log', 'r', encoding='utf-8') as f:
    print(f.readline())
os.mkdir('newdir')
print('Current w dir :', os.getcwd())
