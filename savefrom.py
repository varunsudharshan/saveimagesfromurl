import urllib
import re
import os
#download function
def downloadimgs():
	file1=open('links.txt','r')
	for line in file1:
		line = line[:-1]
		#print os.path.basename(line)
		urllib.urlretrieve(line, os.path.basename(line))
	file1.close()

url = "http://"+raw_input("enter url:\thttp://")	#accept input
f = urllib.urlopen(url)	#get html code
html=f.read()
a=re.compile('<img.*src="(.*\.jpg)"',re.IGNORECASE)	#specify regex
#process source code and write to file
n=a.findall(html)
if not n:
	exit("no images")
file1=open('links.txt','w+')
for i in n:
	i=url+"/"+i
	print i
	file1.write(i+"\n")
file1.close()
print "\nAll links saved in links.txt\n"
#download
while(1):
	choice = raw_input("Do you want to download all the images?(Y/N)")
	if choice=='n' or choice=='N':
		exit()
	elif choice=='y' or choice=='Y':
		downloadimgs()
		exit("Download Complete")
	else:
		print "invalid choice...re-enter choice"