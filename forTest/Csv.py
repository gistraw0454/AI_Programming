def main():
    countries = placeRecordsIntoList("UN.txt")
    countries.sort(key=lambda country: country[3], reverse = True)
    createNewFile(countries)

def placeRecordsIntoList(filename):
    infile = open(filename, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(",")  # 2d list
        listOfRecords[i][2] = eval(listOfRecords[i][2])
        listOfRecords[i][3] = eval(listOfRecords[i][3])
    return listOfRecords

def createNewFile(countries):
    outfile = open("UNbyArea.txt",'w')
    for country in countries:
        outfile.write(country[0] +','+str(country[3])+'\n')
    outfile.close()