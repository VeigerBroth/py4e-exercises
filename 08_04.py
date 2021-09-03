'''Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.'''

file_hander = open('romeo.txt')
unique_words = []

for i in file_hander:
    r_strip = i.rstrip()
    splited = r_strip.split()
    for i in splited:
        if i not in unique_words:
            unique_words.append(i)

print(sorted(unique_words))
    
    
