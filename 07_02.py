"""
Write a program that prompts for a file name, then opens that file and 
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the
lines and compute the average of those values and 
produce an output as shown below. Do not use the sum() 
function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.

Output:
Average spam confidence: 0.7507185185185187
"""

finp = input('Enter file name: ')

fhandler = open(finp)
find_text = 'X-DSPAM-Confidence:'

count_text = 0
float_number = 0
iteration = 0
first_number = 0
second_number = 0

for i in fhandler:
	hm = i.count(find_text)
	if hm == 1:
		count_text+=hm
	hm = i.startswith(find_text)
	if hm == True:
		float_number = float(i[20:len(i)])
		if iteration == 0:
			first_number = float_number
			iteration+=1
		elif iteration == 1:
			second_number = float_number
			second_number+=first_number
			iteration+=1
		elif iteration >= 2:	
			second_number+=float_number
			
print('Average spam confidence:',second_number/count_text)
