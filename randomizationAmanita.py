p1 = open('AmanitaPool.txt', 'r') #pool1
p2 = open('CountryPool.txt', 'r') #pool2
f = open('AmanitaStart.txt', 'r') #input file

import random
import transposer
times = range(3) # number of times for re-sampling 

count = 0
for line in f:
	count +=1 # this will give the number of samples 

number_coord = range(count)
pool1 =[]
for row in p1:
	row=row.strip()
	pool1.append(row)
pool2 =[]
for row in p2:
	row=row.strip()
	pool2.append(row)

#pool 1
g = open('randomAmanitaP1.txt', 'w')
for x in times:
	p1list = []
	for num in number_coord:
		v=random.choice(pool1) #of 100 from p1
		p1list.append(v)

	for thing in p1list:
		g.write(thing + ',')
	g.write('\n')
g.close()

# pool 2
h = open('randomAmanitaP2.txt', 'w')
for x in times:
	p2list = []
	for num in number_coord:
		v=random.choice(pool2) #of 100 from p1
		p2list.append(v)

	for thing in p2list:
		h.write(thing + ',')
	h.write('\n')
h.close()

#transpose the tab delimited file
transposer.transpose(i='randomAmanitaP1.txt', o='outputAmanitaP1.csv')
transposer.transpose(i='randomAmanitaP2.txt', o='outputAmanitaP2.csv')
