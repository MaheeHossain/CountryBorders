# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions to take one country, and to return a list of countries which border it

import csv

from utils import stringifyList

from Text_Printed.errorMessages import TOO_MUCH_DATA
from Text_Printed.bordersOutput import NOT_IN_DATABASE, NO_BORDERS, ONE_BORDER, MULTIPLE_BORDERS

BORDER_FILE = './Borders_database/GEODATASOURCE-COUNTRY-BORDERS.CSV'
MAX_LINES = 2000
COUNTRY_ONE = 1
COUNTRY_TWO = 3

def borders(country):
    # Returns the list of countries that border it, and if country exists

    borderList = []
    match_count = 0

    # Open the border database, check every line to find the correct countries
    with open(BORDER_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Some more lines than there should be
            if (match_count > MAX_LINES):
                print(TOO_MUCH_DATA)
                return stringifyList(borderList)

            # If country is found in database, increment the match count
            # If the matching country isn't empty, it borders - add to list
            if (row[COUNTRY_ONE] == country):
                if (row[COUNTRY_TWO] != ""):
                    borderList.append(row[COUNTRY_TWO])
                match_count += 1
    
    return(borderList, match_count)

def bordersOutput(country):
    # Returns the borders with the required strings

    # Get list of bordering nations, and how many matches database had
    borderList, match_count = borders(country)

    # If country wasn't found in the database
    if (match_count == 0):
        return country + NOT_IN_DATABASE
    
    # If country was in database, but is an island (no bordering nations)
    if (len(borderList) == 0):
        return country + NO_BORDERS

    # If country has a single bordering nation
    elif (len(borderList) == 1):
        return country + ONE_BORDER + stringifyList(borderList)
    
    # If country has multiple bordering nations
    return country + MULTIPLE_BORDERS + stringifyList(borderList)

