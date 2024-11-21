def main():
    countries = placeRecordsIntoList("./file/UN.txt")
    countries.sort(key = lambda country: country[3],reverse=True)
    displayFiveLargestGountrues(countries)
    createNewFile(countries)

def placeRecordsIntoList(fileName):
    infile = open(fileName,'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][2] = eval(listOfRecords[i][2])
        listOfRecords[i][3] = eval(listOfRecords[i][3])
    return listOfRecords

def displayFiveLargestGountrues(countries):
    print("{0:20}{1:9}".format("country","area (sq. mi.)"))
    for i in range(5):
        print("{0:20}{1:9,d}".format(countries[i][0],countries[i][3]))

def createNewFile(countries):
    outfile = open("UNbyArea.txt",'w')
    for country in countries:
        outfile.write(country[0]+','+str(country[3])+"\n")
    outfile.close()

main()