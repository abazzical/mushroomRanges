from collections import defaultdict
from geopy.distance import vincenty

def tabList(list):
	if len(list) == 1:
		row = '\t' + '0'
	else:
		row=''
		for i in list:
			row+= '\t' + str(i)
	return row

cutoff = ['SH0', 'SH1', 'SH2', 'SH3']
geo_sets = ['coords', 'p1001', 'p1002', 'p1003', 'p2001', 'p2002', 'p2003'] # this list represents the columns of the real data and all the other permutations, this list will give the names to the files
# geo_sets = ['coords']

f = open('AmanitaStartRand.txt', 'r') 

data = []
for line in f:
	line =line.strip()
	line=line.split('\t')
	data.append(line)
# print len(data)

posCoordCol = 4 #position of column of the coordinates -1, or in the many iterations version the first column with the coordinates
for geoSet in geo_sets: # name of the run
	posCoordCol += 1
	output = open('SH1'+geoSet+'.txt', 'w') #edit the grouping for naming. this is really up to the user
	dcoord = defaultdict(list) #makes new dictionary
			 
	for dictOfData in range (0, len(data)): #iterates through dictionary
		dcoord[data[dictOfData][2]].append(data[dictOfData][posCoordCol]) #number next to dictOfData is the column position corresponding to the grouping desired (in this case SH1)

	for k,v in dcoord.iteritems():
		output.write( "%s \t %s" % (str(k), str(v)))
		output.write('\n')
	output.close()

# =================================
# Calculate max distance/ range extent
	fastaFile = open('SH1'+geoSet+'.txt','r')
	outputV = open('SH1'+geoSet+'MD.txt','w')
	line1=''
	place = 0
	for line in fastaFile: 
		line = str(line)
		line = line.replace("[", "")
		line = line.replace("]", "")
		line = line.replace("'", "")
		line = line.replace("\n", "")
		list1 = line.split("\t")
		list1[1] = list1[1].replace(', ','$$')	
		list1[1] = list1[1].replace('|',', ')
		list3 = list1[1].split('$$')
		list2 = []
		for i in list3:
			list2.append(i)
		if  len(list2) <= 1:
			listVincenty = [0.0]
		else:
			listVincenty = []
			for thing1 in list2:
				for thing2 in list2:
					distThing12 = vincenty(thing1, thing2).meters
					listVincenty.append(distThing12)
# 	print list2
		listVin = []
		for i in listVincenty: #erases duplicates
			if i not in listVin:
				listVin.append(i)
		name=list1[0]
		V = name + tabList(listVin) + '\n'
		outputV.write(V)
	outputV.close()

	file = open('SH1'+geoSet+'MD.txt','r')
	outMax = open('SH1'+geoSet+'.csv', 'w') # final .csv file with the set of coordinates used, the distance, and grouping
	firstRow = 'treat,dist,SH'+ '\n'
	outMax.write(firstRow)
	for line in file:
		line = str(line)
		a = line.split('\t')
		b = ''
		SH = str(a[0])
		listDist = a[1:]
# 	print listDist
		new_list = []
		for item in listDist:
			item = float(item)
			new_list.append(item)
# 	print new_list	
# 	if len(new_list) == 0:
# 		b = 0
# 	else:
		b = max(new_list)
		b=b/1000
# 	 	print type(b)
		row = geoSet + ',' + str(b) + ',' + SH + '\n'
		outMax.write(row)	
	outMax.close()
