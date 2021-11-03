'''
This program records the domain name (instead of the address) where the 
message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents
of your dictionary.

Sample execution:
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

fh = open('mbox-short.txt')
d = dict()
for i in fh:
    if i.startswith('From ') == True:
        i = i.split()
        i = i[1]
        i = i[i.find('@')+1:len(i)]
        d[i] = d.get(i, 0)+1

print(d)
