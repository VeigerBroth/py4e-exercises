'''
Write a program to read through a mail log, build
a histogram using a dictionary to count how many messages have come
from each email address, and print the dictionary.

Sample execution:
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

Next exercise:
Find who has the most messages and print how many
messages the person has

Sample execution:
cwen@iupui.edu 5
'''

fh = open('mbox-short.txt')
d = dict()
max_value = 0
max_value_key = None
for i in fh:
    if i.startswith('From ') == True:
        i = i.split()
        i = i[1]
        d[i] = d.get(i, 0)+1

for n in d:
    if d[n] > max_value:
        max_value = d[n]
        max_value_key = n

print(f'{max_value_key} {max_value}')
