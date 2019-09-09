# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    b = line.split()
    lst = lst + b
    lst.sort()
newlst = list()
notlst = list()
i = 0
for word in lst:
    if i >= (len(notlst)+len(newlst)):
        if i == 0:
            newlst.append(lst[0])
            i = i+1
        elif lst[i - 1] != lst[i]:
            newlst.append(lst[i])
            i = i+1
        elif lst[i - 1] == lst[i]:
            notlst.append(lst[i])
            i = i + 1
    elif i == (len(lst)):
        break
print(newlst)