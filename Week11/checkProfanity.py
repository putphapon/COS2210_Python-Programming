import urllib.request, urllib.parse

#read texts in a file
def read_text(fileName):  
    quotes = open(fileName)
    contents_of_file = quotes.read()
    quotes.close()
    return contents_of_file

contents = read_text('quote.txt')

url_name = "http://www.wdylike.appspot.com/?q="+urllib.parse.quote(contents)
connection = urllib.request.urlopen(url_name) 
output = connection.read()
connection.close()

if 'true' in str(output):
  print("profanity Alert!!!")
else:
  print("This document has no curese words!")


