The program will use urllib to read the HTML from the data files below,
extract the href= values from the anchor tags,
scan for a tag that is in a particular position from the top and follow that link,
repeat the process a number of times, and report the last name you find.

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Bailley.html
Find the link at position 18 (the first name is 1). Follow that link.
Repeat this process 7 times. The answer is the last name that you retrieve.
The first character of the name of the last page that you will load is: I
