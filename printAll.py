import csv
import sys

BORDER_FILE = 'GEODATASOURCE-COUNTRY-BORDERS.CSV'
MAX_LINES = 2000
COUNTRY_ONE = 1
COUNTRY_TWO = 3

def stringifyList(list):
    string = ""
    
    for item in list:
        string += item + ", "

    return string[:-2]

def borders(country):
    # prints the list of countries that border it
    borderList = []

    with open(BORDER_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (line_count > MAX_LINES):
                # Some more lines than there should be
                print("Too much data in file - error")
                return stringifyList(borderList)
            if (row[COUNTRY_ONE] == country):
                if (row[COUNTRY_TWO] != ""):
                    borderList.append(row[COUNTRY_TWO])
                line_count += 1

    if (len(borderList) == 0):
        return country + " borders no countries"
    elif (len(borderList) == 1):
        return country + " borders this country: " + stringifyList(borderList)
    return country + " borders these countries: " + stringifyList(borderList)

if __name__ == '__main__':
    fptr = sys.stdout

    country = input().strip()
    result = borders(country)
    fptr.write(result + '\n')

    fptr.close()