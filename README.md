# mushroomRanges

I wrote these scripts to calculate the range extent of mushroom OTUs. 
This means that they take the geolocation of a group of specimens, calculate the distance between all pairs, and spit out the largest distance.
I have included example files to run the scripts. 

Python packages used:
geopy
transposer
random
defaultdict

The scripts have a lot of print messages I used to check if it was working properly, and I have not removed the intermediate file outputs for the same reason. Those intermediate files are super ugly.

(i) AmanitaMaxdist4loop1.py - just one set of coordinates for samples 
Input file:'AmanitaStart.txt' is a tab-delimited file where each row is a sample with some information about the sample and the group it belongs to. By 'group' I mean OTU, but it could be any grouping you would like. Groupings or sample accessions could be OTUs or species or just any group of specimens.

The columns in the input file are:

Genus\t coordinates\t SH0\t SH1\t SH2\t SH3
e.g.
Amanita\t -18.766947|46.869107\t SH380322.07FU\t SH104846.07FU\t SH053318.07FU\t SH015084.07FU

(but you can put whatever, as long as the coordinates are there, it should work)

If you want to change the number of groupings you can edit line 13 of 'AmanitaMaxdist4loop1.py' defining the cutoff. The script as it is says 'cutoff = ['SH0', 'SH1', 'SH2', 'SH3']'

Just range extent of 'SH1' of 'AmanitaStart.txt' run:
AmanitaMaxdist4loop1.py

It outputs 3 files, the .csv file is the one with the range extents.


(ii) AmanitaMaxdist4loop2.py - several sets of coordinates for the same samples - Input file can include permutations or randomizations, although it means more fiddling. At the end though, it does exactly the same thing as the previous script.

For this analysis I wanted to permute and randomize the data. So each of the samples was re-assigned a coordinate randomly from two pools of coordinates.

To get permutations/randomizations:
For my analysis I used two 'pools'. From one I randomly sampled from the same coordinates as the original file 'AmanitaStart.txt'. The second one samples from coordinates from all countries of the world. 
Permutation 'AmanitaPool.txt'
Randomization 'CountryPool.txt'

Script 'randomizationAmanita.py' assigns to each sample a coordinate and outputs two sets one per pool.
outputAmanitaP1.txt
outputAmanitaP2.txt

'AmanitaStart.txt' can include more columns with permutations or randomizations. See 'AmanitaStartRand.txt' for format.

Looks like this:
Genus\t coordinates\t SH0\t SH1\t SH2\t SH3\t permutation1\t permutation2\t permutation3...

Range extents of the observed data and the re-sampled data run 'AmanitaMaxdist4loop2.py'

Running it will output 3 files per set (column) of coordinates, .csv contains the range extents (again, the other files are uggos).


(iii) Other scripts related to the range extents include: remove singleton OTUs (cleanDataafterRandom.py), how many samples are there in an OTU? (countSamplesInOTU.py), count singletons (countSinglesDataafterRandom.py)


(iv) For the analysis I also calculated the average genetic distances of samples in an OTU based on their ITS sequence. The input file for this script includes the sequence in one of the columns, there is an example of the host tree data 'bySHGenHost.txt'. This script requires mafft installed, packages collections, cogent, and numpy.
This script makes a fasta file based on the grouping of your choice, passes it through mafft to get an alignment, then gets a distance matrix, then parses through the distance matrix to get the average. It outputs everything in a csv file.

The input files are using data from the UNITE fungal database:
Abarenkov, K., Nilsson, R.H., Larsson, K.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., Larsson, E., & Pennanen, T. 2010. The UNITE database for molecular identification of fungi–recent updates and future perspectives. New Phytol. 186:281-285.
Kõljalg, U., Larsson, K.H., Abarenkov, K., Nilsson, R.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., & Larsson, E. 2005. UNITE: a database providing web‐based methods for the molecular identification of ectomycorrhizal fungi. New Phytol. 166:1063-1068.

How unlikely that you would read until the end! If you looked at the scripts, you can guess from the clumsy code that I am not a computer scientist. These scripts don't do anything particularly fancy, they are here for the sake of transparency and while I tried to make them reasonably understandable, I was not writing them as a tool for general use. If you intend to use the scripts on your files, please change them so that they will work for your files. Get in touch if you would like more information about the analysis.

