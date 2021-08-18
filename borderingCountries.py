import csv

from utils import stringifyList

BORDER_FILE = './Borders_database/GEODATASOURCE-COUNTRY-BORDERS.CSV'
MAX_LINES = 2000
COUNTRY_ONE = 1
COUNTRY_TWO = 3

# def borderOfBorders(country_list):
#     secondRankBorders = []
#     for country in country_list:
#         borderList, line_count = borders(country)
#         if (line_count == 0):
#             print()
#         return 0

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
                print("Too much data in file - error")
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
        return country + " not present in database"
    if (len(borderList) == 0):
        return country + " borders no countries"
    elif (len(borderList) == 1):
        return country + " borders this country: " + stringifyList(borderList)
    return country + " borders these countries: " + stringifyList(borderList)