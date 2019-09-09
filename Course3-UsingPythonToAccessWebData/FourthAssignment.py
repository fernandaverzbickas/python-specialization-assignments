# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for 
# a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times
# and report the last name you find.

#Desired Outputs
# Sample problem: Enter the URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter Count: 4
# Enter Position: 7
# ---> Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Chenille.html
# Enter Count: 7
# Enter Position: 18
# ---> Last name in sequence: Grzegorz



from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
count = input("Enter count: ")
position = input("Enter position: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
n = 0
while n < int(count):
    for tag in tags:
        if tag == tags[int(position) - 1]:
            print('n:',n )
            nextperson = tag.get('href', None)
            contents = tag.contents[0]
            print('URL:', nextperson)
            print('Contents:', contents)
            url = nextperson
            html = urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup('a')
            n = n + 1
            if n == int(count): break
    