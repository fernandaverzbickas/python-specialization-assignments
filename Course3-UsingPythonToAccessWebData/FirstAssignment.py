# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_291734.txt (There are 81 values and the sum ends with 668)

# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 


import re
fle = input('Enter text file:')
handle = open(fle)

wholetxt = list()
for line in handle:
    line = line.rstrip()
    setofwords = line.split()
    wholetxt = wholetxt + setofwords
wholetxt = str(wholetxt)
numbers = re.findall('[0-9]+', wholetxt)
total = 0
for num in numbers:
    intnum = int(num)
    total = total + intnum
print(total)

#Desired outputs:
#For (regex_sum_42.txt) = 445833
#For (regex_sum_291734.txt) = 373668
