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

(i)Just one set of coordinates for samples - Input file 1:

'AmanitaStart.txt' is a tab-delimited file where each row is a sample with some information about the sample and the group it belongs to. By 'group' I mean OTU, but it could be any grouping you would like. Groupings or sample accessions could be OTUs or species or just any group of specimens.

The columns in the input file are:

Genus\t coordinates\t SH0\t SH1\t SH2\t SH3
e.g.
Amanita\t -18.766947|46.869107\t SH380322.07FU\t SH104846.07FU\t SH053318.07FU\t SH015084.07FU

(but you can put whatever, as long as the coordinates are there, it should work)

If you want to change the number of groupings you can edit line 13 of 'AmanitaMaxdist4loop1.py' defining the cutoff. The script as it is says 'cutoff = ['SH0', 'SH1', 'SH2', 'SH3']'

Just range extent of 'SH1':
AmanitaMaxdist4loop1.py

outputs 3 files, the .csv file is the one with the range extents.


(ii) Several coordinates for the same samples - Input file 2-step (with permutations or randomizations means more fiddling, but this does exactly the same thing as the previous script):

For this analysis I wanted to permute and randomize the data. So each of the samples was re-assigned a coordinate randomly from two pools of coordinates.


To get permutations/randomizations:
For my analysis I used two pools, one with the same coordinates as the original file AmanitaStart.txt, one with coordinates from all countries of the world.
But you should use what you think is appropriate.
Permutation 'AmanitaPool.txt'
Randomization 'CountryPool.txt'

Script assigns to each sample a coordinate

outputAmanitaP1.txt
outputAmanitaP2.txt

Brute-force or elegant R, just get a file that has the original 'AmanitaStart.txt' but with more columns with permutations. See AmanitaStartRand.txt for format:

Genus\t coordinates\t SH0\t SH1\t SH2\t SH3\t permutation1\t permutation2\t permutation3...

Range extents of the observed data and the re-sampled data:
AmanitaMaxdist4loop2.py

outputs 3 files per set, .csv are the contain the range extents (again, the other files are uggos).

(iii)
other scripts for things include: remove singleton OTUs (cleanDataafterRandom.py), how many samples are there in an OTU? (countSamplesInOTU.py), count singletons (countSinglesDataafterRandom.py)

The input files are using data from the UNITE fungal database:
Abarenkov, K., Nilsson, R.H., Larsson, K.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., Larsson, E., & Pennanen, T. 2010. The UNITE database for molecular identification of fungi–recent updates and future perspectives. New Phytol. 186:281-285.
Kõljalg, U., Larsson, K.H., Abarenkov, K., Nilsson, R.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., & Larsson, E. 2005. UNITE: a database providing web‐based methods for the molecular identification of ectomycorrhizal fungi. New Phytol. 166:1063-1068.


How unlikely that you would read until the end! If you looked at the scripts, you can guess from the clumsy code that I am not a computer scientist. They are here for the sake of transparency and while I tried to make them understandable, I was not writing them as a tool for general use. Get in touch if you would like more information about the analysis, and you can also read the paper here:

