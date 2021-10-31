'''
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a
string is in the dictionary.
'''

fh = open('words.txt')
dict_words = dict()
values = 0
for words in fh:
    for i in words.split():
        values+=1
        dict_words = {i: values}
        print(dict_words)
