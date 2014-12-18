with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[6] < line[3]:
#        if line[3] < line[4]:
            print line