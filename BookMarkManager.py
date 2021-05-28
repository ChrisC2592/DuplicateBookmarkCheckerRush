def Notes():
# Bookmark manager idea thought page
# #[IGNORE] just getting the title a method could be
	# method 1:
		# .rstrip("</A>") to get rid of the ending anchor tag then
		# use rsplit(">") to create a list
		# and the third item in the list will be the title of the website 
		# using this we could make a list or dictionary using a loop of some kind
		# to have every title be added
# #[IGNORE]Openning file trial & error
	#infile = open("test.txt", "r", -1, None, "ignore")
#	x = infile.readlines()
#	i = 0
#	for line in x:
#		print(x[i])
#		i = i + 1#yay we can now read and print the file
# #OBTAIN URL 
#	sbody.a.string #using randomVariable.a.body can get the content of the a tag for a line #mass scale version or better way ?
# 	'BanchoLeomon - Digimon Wiki: Go on an adventure to tame the frontier and save the fused world!'
# 	for link in sbody.find_all('a'):#found online get the href value from within the <a> tag 
# 	...     print(link.get('href'))#Dont know how that works but glad found it #http://digimon.wikia.com/wiki/BanchoLeomon

# def isDuplicateTitle(soupList):
	# i, title = 0, 0 #make seperate module to check url
	# title, href, sLine = "","",0
	# duplicates = []
	# primerDupli = False
	# primer = 
	# i +=1
	# for i in soupList:
		# title, href, sLine = soupList[i]
		# if primer == :
			# primerDupli = True
	# if primerDupli == True:
		# duplicates.append(primer)
		# if len(soupList) != 0:
			# primer = soupList[0]#set equal to top of list
	# return
	return
from bs4 import BeautifulSoup,UnicodeDammit
import string, re

def openFile(inFile):
	soup = BeautifulSoup(open(inFile, encoding="utf8"), "html5lib")
	return soup
def closeFile(soup):
	#outfile = open(, "w")
	# print(soup.encode('utf8', formatter="html5"), file=outfile)
	with open("testx.html", "w", encoding="utf-8") as f:
		f.write(soup.prettify(formatter="html5"))
	f.close
	return False
def findFolder(tag):
	tagFolder = ""
	if tag.name == 'a':
		tag = tag.parent
	if tag.parent.name == 'dl':
		if tag.parent.parent.name =="dt":
			tagFolder = tag.parent.parent.h3.string
	return tagFolder
def findTagInfo(aTags):
	tagData = []
	for tag in aTags:
		tagData.append((tag.string, tag.get('href'), findFolder(tag), tag.sourceline, tag.parent))
	return tagData
def isDuplicateURL(tagData):
	occurences = []
	
	for tag in tagData:
		count = 0
		i = 0
		pTitle,pHref,pFolder,pSLine,pDT = tag
		for x in tagData:
			tTitle,tHref,tFolder,tSLine,tDT = tagData[i]
			if pHref == tHref:
				count += 1
			i += 1
		occurences.append(count)
		
	duplicates = set()
	index = 0
	while index < len(tagData):
		if occurences[index] != 1:
			duplicates.add(tagData[index])
		index += 1
	return duplicates
def getUserChoice(duplicateSet):
	duplicates = []
	index = 0
	choice=""
	control = True
	for x in duplicateSet:
		duplicates.append(x)
	
	print(duplicates, len(duplicates))
	
	while control == True:
		print("Confirm Deletion")
		print("enter the digit of any bookmark you want to keep")
		for x in duplicates:
			print(count + ")  " + x)
		
		#choice = input()#testing
		
		# if type(choice) == str and choice != 'exit':
			# print('bee boop~ please enter a valid value or "exit" to exit ~boop bop')
		
		try:
			if int(choice) <= len(duplicates) and int(choice) >= 0:
					duplicates.remove(duplicates[int(choice)])
			elif choice == 'exit':
				control = False
		except:
			print('Please enter a valid value or "exit" to exit')
		control = False#testing
	return duplicates
def removeDuplicate(soup,duplicates):
	tempResults = []
	#print(len(soup.a))
	for x in duplicates:
		pTitle,pHref,pFolder,pSLine,pDT = x
		counter = 0
		# sHref = '"'+"a[href="+pHref+"]"+'"'
		# print(sHref)
		tempResults = soup.find_all(string=pDT.a.string)
		# print(tempResults)
		for index in tempResults:
			#print(index.parent.sourceline,pSLine)
			if pSLine == index.parent.sourceline:
				index.parent.parent.decompose()
	return soup
def main():
	inFile = "bookmarks.html"
	soup = openFile(inFile)
	
	anchorTags = soup.find_all('a')
	tagData = findTagInfo(anchorTags)
	duplicateURL = isDuplicateURL(tagData)
	duplicateURL = getUserChoice(duplicateURL)
	soup = removeDuplicate(soup,duplicateURL)
	closeFile(soup)
	
main()