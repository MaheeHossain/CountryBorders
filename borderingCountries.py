import csv

from utils import stringifyList

from Text_Printed.errorMessages import TOO_MUCH_DATA, BORDERING_COUNTRY_NO_DATA
from Text_Printed.bordersOutput import NOT_IN_DATABASE, NO_BORDERS, ONE_BORDER, MULTIPLE_BORDERS, NO_SECOND_BORDERS, ONE_SECOND_BORDERS, MULTIPLE_SECOND_BORDERS

BORDER_FILE = './Borders_database/GEODATASOURCE-COUNTRY-BORDERS.CSV'
MAX_LINES = 2000
COUNTRY_ONE = 1
COUNTRY_TWO = 3

def borderOfBorders(originalCountry, lines, country_list):
    secondRankBorders = []
    if (lines == 0):
        return secondRankBorders
    for country in country_list:
        borderList, line_count = borders(country)
        if (line_count == 0):
            print(BORDERING_COUNTRY_NO_DATA)
        for secondaryCountry in borderList:
            if ((secondaryCountry not in secondRankBorders) and secondaryCountry != originalCountry):
                secondRankBorders.append(secondaryCountry)
    return secondRankBorders

def borders(country):
    # Returns the list of countries that border it, and if country exists
    borderList = []
    line_count = 0
    # Open the border database, check every line to find the correct countries
    with open(BORDER_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (line_count > MAX_LINES):
                # Some more lines than there should be
                print(TOO_MUCH_DATA)
                return stringifyList(borderList)
            if (row[COUNTRY_ONE] == country):
                if (row[COUNTRY_TWO] != ""):
                    borderList.append(row[COUNTRY_TWO])
                line_count += 1
    
    return(borderList, line_count)

def bordersOutput(country):
    # Returns the borders with the required strings
    borderList, line_count = borders(country)
    if (line_count == 0):
        return country + NOT_IN_DATABASE
    if (len(borderList) == 0):
        return country + NO_BORDERS
    elif (len(borderList) == 1):
        return country + ONE_BORDER + stringifyList(borderList)
    return country + MULTIPLE_BORDERS + stringifyList(borderList)

def secondaryBordersOutput(country):
    # Returns the secondary borders with the required strings
    borderList, line_count = borders(country)
    secondBorderList = borderOfBorders(country, line_count, borderList)
    if (len(secondBorderList) == 0):
        return country + NO_SECOND_BORDERS
    elif (len(secondBorderList) == 1):
        return country + ONE_SECOND_BORDERS + stringifyList(secondBorderList)
    return country + MULTIPLE_SECOND_BORDERS + stringifyList(secondBorderList)