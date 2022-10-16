
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input ('Enter html: ')
count=0
pos = input ('Enter position: ')
nmb = input ('Enter count: ') # desired amount of cycle repetitions

while count<int(nmb):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    list1=list()
    tags = soup('a') # Retrieve all of the anchor tags

    for tag in tags:
        list1.append(tag.get('href', None))

    url=list1[int(pos)-1]
    count+=1
    print ('Retreiving:',url)
