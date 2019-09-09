#Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers
# in the file and enter the sum below:

# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_291739.json (Sum=3005)



import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL:')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

info = json.loads(data)
print('User count:', len(info['comments']))

tot = 0
for item in info['comments']:
    count = item['count']
    tot = tot + count
print(tot)