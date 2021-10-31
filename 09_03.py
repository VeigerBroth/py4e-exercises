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
'''

fh = open('mbox-short.txt')
d = dict()
for i in fh:
    if i.startswith('From ') == True:
        i = i.split()
        i = i[1]
        d[i] = d.get(i, 0)+1

print(d)
