#/usr/bin/python

import re,urllib

textfile = file('crawler-tmp.txt')
print "Enter the URL to crawl"
print 'Usage "http://guilhermecardoso.pt" <-- with double quotes!'
url=input("@>")
#url="http://www.guilhermecardoso.pt"
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(url).read(), re.I):
        print i  
        textfile.write(i+'\n')
textfile.close()

# just an quick example for me to learnr python :)