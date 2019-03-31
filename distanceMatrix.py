
from collections import defaultdict
from cogent import LoadSeqs
from cogent.phylo import distance
from cogent.evolve.models import GTR
import numpy
# ========
# make a dictionary from tab delimited file
file = open('GenHost.txt', 'r')	
# 	d=mushroomSH.tabToDict(file) # takes tab-delimited file and turns into a dictionary
data = []
for line in file:
	line =line.strip()
	line=line.split('\t')
	data.append(line)
# 	print line
# print len(data)
output = open("bySHGenHost.txt",'w')
dcoord = defaultdict(list) #makes new dictionary
for accno, sh_code, genus, fast in data:
# for nic in range (0, len(data)):
# 				
	dcoord[sh_code].append(fast) # this is the part that would be helpful if it looped

for k,v in dcoord.iteritems():
	output.write( "%s \t %s" % (str(k), str(v)))
	output.write('\n')
output.close()
# 
# ### calculate max distance?
fastaFile = open("bySHGenHost.txt",'r')
GenDist = open("SH1genDistGenHost.csv", 'w')
line1=''
place = 0
for line in fastaFile:
	line = str(line)
	line = line.replace("[", "")
	line = line.replace("]", "")
	line = line.replace("'", "")
	list1 = line.split("\t")
	list1[0] = list1[0].strip()
	outputV = open(str(list1[0])+".fasta",'w')
	list1[1] = list1[1].strip()
	list1[1] = list1[1].replace(', ','$$')	# replace the \t 1 \t	 or split directly?
	list1[1] = list1[1].replace('$$','\n')
# 	print list1[1]
	list11 = str(list1[1])
	outputV.write(list11)
	outputV.close()

# 
# # ========
# # install mafft to output the alignment of the sequences
# # I can see this failing majorly on your machine if you cannot call mafft from anywhere
	import subprocess
	subprocess.call(['mafft '+str(list1[0])+'.fasta > '+str(list1[0])+'align.fasta'], shell=True)
# 
# ========
# take aligned fasta file and get a distance matrix
	al = LoadSeqs(list1[0]+"align.fasta")
	dist = distance.EstimateDistances(al, submodel = GTR())
	dist.run()
	print dist
	dist.writeToFile('dist'+list1[0]+'.phylip')

# ========
# take distance matrix, input it as an array and 
	phylipo = open('dist'+list1[0]+'.phylip', 'r')
	phylist = []
	firstDone = False
	line1=''
	for line in phylipo:
		line = line.strip()
		if not firstDone:
			firstDone = True
		else:
			if line[0] != ' ':
				line = '\n' + line
			else:
				line = line.replace('\n','')
			line1 = line1 + line
		list2 = line1.split('\n')
# 		print list2
		for phyline in list2:
			phyline = phyline.replace('        ', '$$')
			phyline = phyline.replace('       ', '$$')
			phyline = phyline.replace('      ', '$$')
			phyline = phyline.replace('     ', '$$')
			phyline = phyline.replace('   ', '$$')
			phyline = phyline.replace('  ', '$$')
			phyline = phyline.split('$$')
			phyline = phyline[1:]
			for phyitem in phyline:
				phyitem = float(phyitem)
				phylist.append(phyitem)

	med = numpy.median(phylist)
	avg = numpy.average(phylist)
	max = numpy.max(phylist)
	print med, avg, max
	outLine = str(list1[0]) + ',' + str(med)+ ',' +str(avg)+ ',' +str(max)+ '\n'
	print outLine
	GenDist.write(outLine)



