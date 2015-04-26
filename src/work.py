#!/usr/bin/python


import mmh3
import json
from collections import Counter
from collections import defaultdict
import urllib
import ast


def getHash(word):
	'''
		This return the hash value and does the anding with 0xffffffffL on a 32 bit system
	'''
	curHash = mmh3.hash(word)
	curHash = curHash & 0xffffffffL
	return curHash

'''
def similaritySignature(word):
	myDict = collections.Counter(word) #word frenquency dictionary
	key, value = myDict.popitem()
	concatStr = key + str(value)
	curHash = getHash(concatStr)
	negMinimum = curHash 
	for key,value in myDict.iteritems():
		concatStr = key + str(value)
		curHash = getHash(concatStr)
		if ( curHash < negMinimum ):
	   		negMinimum = curHash

	return negMinimum   		
'''


def similaritySignature(sentence):
	'''
		This done using the locality sensitive hashing
	'''
	myList = Counter(sentence.split()).most_common() #word frenquency dictionary
	key, value = myList[0]
	concatStr = key + str(value)
	curHash = getHash(concatStr)
	negMinimum = curHash 
	for key,value in myList[1:]:
		concatStr = key + str(value)
		curHash = getHash(concatStr)
		if ( curHash < negMinimum ):
	   		negMinimum = curHash

	return negMinimum  



def formatJsonObject(filename):
	'''
	format the json string with a comma for each item
	'''
	data = ""
	with open(filename) as myfile:    
		data = myfile.read()	
		data = data.replace('\n', ',')

	data = data[:-1]


	#return ast.literal_eval(data)[0]["model"]
	return ast.literal_eval(data)



def getProductNameWithSignature(filename): 
	dataSource = formatJsonObject(filename)
	totalData = {}
	for obj in dataSource:
		prodName = obj["product_name"]
		prodManufacturer = obj["manufacturer"]
		neededString = prodName +" "+ prodManufacturer 
		#neededString = prodName 
		hashValue = similaritySignature(neededString)
		totalData[hashValue] = prodName
	return totalData



def getTitleWithSignature(filename): 
	dataSource = formatJsonObject(filename)
	totalData = defaultdict(list)

	for obj in dataSource:
		prodTitle = obj["title"]
		prodManufacturer = obj["manufacturer"]
		neededString = prodTitle +" "+ prodManufacturer 
		#neededString = prodTitle 
		hashValue = similaritySignature(neededString)
		totalData[hashValue].append(obj)
	return totalData



def combineData(prodFile, listFile ):
	prodObj = getProductNameWithSignature(prodFile)
	listObj = getTitleWithSignature(listFile)
	
	totalDataSet = []
	for currentHashVal, prodName in prodObj.iteritems():
		totalData = {}
		listingList = listObj[currentHashVal]
		totalData["product_name"] = prodName
		totalData["listings"] = listingList 
		if listingList :
			totalDataSet.append(totalData)

	return totalDataSet




def writeToFile():
	prodFile = "products.txt"
	listFile = "listings.txt"
	data = combineData(prodFile, listFile )

	#for item in data:
	#	with open('output.txt', 'w') as f:
	#		f.write("%s\n" % json.dumps(item))

	with open('output.txt', 'w') as f:
		f.write("%s\n" % json.dumps(data))


if __name__ == "__main__":
    #print (getHash("two.py is being run directly"))
    writeToFile()





    









