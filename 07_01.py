fhandler = open('mbox-short.txt')

for i in fhandler:
    a = i.rstrip()
    print(a.upper())
