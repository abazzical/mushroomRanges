from collections import defaultdict

f = open('mushroomInput.txt', 'r')
data = []
for line in f:
	line =line.strip()
	line=line.split('\t')
	data.append(line)
	
#print data


findSingles = defaultdict(list)
for Genus, coord, SH0, SH1, SH2, SH3, p1001, p1002, p1003, p1004, p1005, p1006, p1007, p1008, p1009, p1010, p1011, p1012, p1013, p1014, p1015, p1016, p1017, p1018, p1019, p1020, p1021, p1022, p1023, p1024, p1025, p1026, p1027, p1028, p1029, p1030, p1031, p1032, p1033, p1034, p1035, p1036, p1037, p1038, p1039, p1040, p1041, p1042, p1043, p1044, p1045, p1046, p1047, p1048, p1049, p1050, p1051, p1052, p1053, p1054, p1055, p1056, p1057, p1058, p1059, p1060, p1061, p1062, p1063, p1064, p1065, p1066, p1067, p1068, p1069, p1070, p1071, p1072, p1073, p1074, p1075, p1076, p1077, p1078, p1079, p1080, p1081, p1082, p1083, p1084, p1085, p1086, p1087, p1088, p1089, p1090, p1091, p1092, p1093, p1094, p1095, p1096, p1097, p1098, p1099, p1100, p2001, p2002, p2003, p2004, p2005, p2006, p2007, p2008, p2009, p2010, p2011, p2012, p2013, p2014, p2015, p2016, p2017, p2018, p2019, p2020, p2021, p2022, p2023, p2024, p2025, p2026, p2027, p2028, p2029, p2030, p2031, p2032, p2033, p2034, p2035, p2036, p2037, p2038, p2039, p2040, p2041, p2042, p2043, p2044, p2045, p2046, p2047, p2048, p2049, p2050, p2051, p2052, p2053, p2054, p2055, p2056, p2057, p2058, p2059, p2060, p2061, p2062, p2063, p2064, p2065, p2066, p2067, p2068, p2069, p2070, p2071, p2072, p2073, p2074, p2075, p2076, p2077, p2078, p2079, p2080, p2081, p2082, p2083, p2084, p2085, p2086, p2087, p2088, p2089, p2090, p2091, p2092, p2093, p2094, p2095, p2096, p2097, p2098, p2099, p2100 in data:

	findSingles[SH1].append(coord)

#print findSingles

outputSIng = open("howManyInOTU.txt",'w')
# output = open("PNWSH1.txt",'w')
# singleList = []
notSingle = []
# length_key = len(d['findSingles'])
for i in findSingles:
	howMany = str(len(findSingles[i]))
	outputSIng.write(i+'\t'+howMany+'\n')


# output.close()
outputSIng.close()
# print singleList