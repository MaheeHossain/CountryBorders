import csv
import sys

BORDER_FILE = './Borders_database/GEODATASOURCE-COUNTRY-BORDERS.CSV'
INPUT_FILE = 'Input.txt'
MAX_LINES = 2000
COUNTRY_ONE = 1
COUNTRY_TWO = 3

def stringifyList(list):
    string = ""
    
    for item in list:
        string += item + ", "

    return string[:-2]

def readInput():
    # Reads the input file and returns an array with all countries
    lines=[]
    with open(INPUT_FILE) as f:
        lines = f.readlines()
    return lines

def removeNewLine(string):
    # If string has new line at the end, remove it
    if (string[-1] == '\n'):
        return string[:-1]
    return string

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
        if (line_count == 0):
            return country + " not present in database"

    if (len(borderList) == 0):
        return country + " borders no countries"
    elif (len(borderList) == 1):
        return country + " borders this country: " + stringifyList(borderList)
    return country + " borders these countries: " + stringifyList(borderList)

if __name__ == '__main__':
    fptr = sys.stdout

    countries = readInput()
    for country in countries:
        result = borders(removeNewLine(country))
        fptr.write(result + '\n')

    fptr.close()