# mushroomRanges

I wrote these scripts for calculating the range extent of mushroom OTUs.

Python packages used:
geopy
transposer
random
defaultdict

The scripts have a lot of print messages I used to check if it was working properly, and I have not removed the intermediate file outputs for the same reason.

(i)
Just one set of coordinates - Input file 1:
AmanitaStart.txt
tab-delimited file
Groupings or sample accessions could be OTUs, species. Just the group of specimens you want to calculate the range extent.

Genus\t coordinates\t SH0\t SH1\t SH2\t SH3
e.g.
Amanita\t -18.766947|46.869107\t SH380322.07FU\t SH104846.07FU\t SH053318.07FU\t SH015084.07FU

Just range extent of 1 grouping:
AmanitaMaxdist4loop1.py

outputs 3 files, the .csv file is the one with the range extents.


(ii)
Several coordinates for the same samples - Input file 2-step (with Randomizations means more fiddling):

To get randomizations:
Two pools I used, one with the same coordinates as the original file AmanitaStart.txt, one with coordinates from all countries of the world.
But you should use what is appropriate for your sampling.
AmanitaPool.txt
CountryPool.txt

Script assigns to each sample a coordinate

outputAmanitaP1.txt
outputAmanitaP2.txt

Brute-force or elegant R, just get a file that has the original 'AmanitaStart.txt' but with more columns with permutations. See AmanitaStartRand.txt for format:

Genus\t coordinates\t SH0\t SH1\t SH2\t SH3\t permutation1\t permutation2\2 permutation3...

Range extents of the observed data and the re-sampled data:
AmanitaMaxdist4loop2.py

outputs 3 files per set, .csv are the contain the range extents

(iii)
other things include: remove singletons (cleanDataafterRandom.py), how many samples are there in an OTU? (countSamplesInOTU.py), count singletons (countSinglesDataafterRandom.py)

The input files are using data from the UNITE fungal database:
Abarenkov, K., Nilsson, R.H., Larsson, K.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., Larsson, E., & Pennanen, T. 2010. The UNITE database for molecular identification of fungi–recent updates and future perspectives. New Phytol. 186:281-285.
Kõljalg, U., Larsson, K.H., Abarenkov, K., Nilsson, R.H., Alexander, I.J., Eberhardt, U., Erland, S., Høiland, K., Kjøller, R., & Larsson, E. 2005. UNITE: a database providing web‐based methods for the molecular identification of ectomycorrhizal fungi. New Phytol. 166:1063-1068.

