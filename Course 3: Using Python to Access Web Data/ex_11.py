#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Actual data: http://py4e-data.dr-chuck.net/regex_sum_38794.txt 

#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the integers.

import re
file = open('regex_sum_38794.txt')
sum=0

for line in file:
    line = line.rstrip()
    # print(line)
    output = re.findall('[0-9]+',line)
    if len(output) > 0:
        # print(output)
        for number in output:
            sum = sum + int(number)

print(sum)
