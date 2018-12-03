import csv, json, sys, glob, os
    
fileOutput = 'output.csv'
    
writeIt = []
counter = 0
    
outputFile = open(fileOutput, 'w')

for root, dirs, files in os.walk('lastfm_subset'):
	for filename in files:
		fileInput = os.path.join(root, filename)
		inputFile = open(fileInput)
		data = json.load(inputFile)
		inputFile.close()
		
		allValues = data.values()
		allKeys = data.keys()
		
		output = csv.writer(outputFile)
		
		if(counter == 0):
			output.writerow([allKeys[3]] + [allKeys[4]] + [allKeys[1]])
			counter += 1
		
		writeIt = [allValues[3].encode('utf-8')] + [allValues[4]] + [allValues[1]]
		
		output.writerow(writeIt)
