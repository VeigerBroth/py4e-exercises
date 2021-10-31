'''
Write a program that categorizes each mail message by which day of the
week the commit was done. To do this look for lines that start with
 “From”, then look for the third word and keep a running count of
 each of the days of the week. At the end of the program print out the
  contents of your dictionary (order does not matter).
  
  Sample line:
  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

  Sample execution:
  {'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

fh = open('mbox-short.txt')
d = dict()
for i in fh:
    if i.startswith('From ') == True:
        i = i.rstrip()
        i = i.split()
        i = i[2]
        d[i] = d.get(i, 0)+1
            
print(d)
