# Variables to use with header
continent = line[0]
elevationZone = line[1]
urbanOrRural = line[2]
pop1990 = line[3]
pop2000 = line[4]
Pop2010 = line[5]
pop2100 = line[6]
landArea = line[7]

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        print Continent, landArea