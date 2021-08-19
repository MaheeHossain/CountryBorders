# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions to take a list of countries, and to return a list of countries
# which border them that are not in the original list

from utils import stringifyList
from borderingCountries import borders

from Text_Printed.errorMessages import BORDERING_COUNTRY_NO_DATA
from Text_Printed.bordersOutput import NOT_IN_DATABASE_ORDINAL, NO_ORDINAL_BORDERS, ONE_ORDINAL_BORDERS, MULTIPLE_ORDINAL_BORDERS, NO_TERTIARY_BORDERS, ONE_TERTIARY_BORDERS, MULTIPLE_TERTIARY_BORDERS

EXISTS_FLAG       = True
DOESNT_EXIST_FLAG = False

def borderOfBorders(originalCountries, lines, country_list):
    # Returns list of countries which border the originalcountries list
    # Can make this work for all numbers, not just 2

    ordinalRankBorders = []
    # Make a list of all countries already outputted
    blackList = originalCountries + country_list

    # If country does not exist, return an empty list
    # This will make countries that don't exist give same output as 
    # countries with no borders. Possible fix is to include a flag
    if (lines == 0):
        return ordinalRankBorders, DOESNT_EXIST_FLAG
    
    # Go through country_list
    for country in country_list:
        borderList, line_count = borders(country)

        # If a country bordering the original data can't be found
        # in the database, print an error
        if (line_count == 0):
            print(BORDERING_COUNTRY_NO_DATA)
        
        # Check if each country bordering this bordering nation is in 
        # original lists or in ordinal country list, if not then append
        for ordinalCountry in borderList:
            if ((ordinalCountry not in blackList) and 
                (ordinalCountry not in ordinalRankBorders)): 
                ordinalRankBorders.append(ordinalCountry)

    return ordinalRankBorders, EXISTS_FLAG

def ordinalBordersOutput(country, ordinalValue):
    # Returns the secondary borders with the required strings

    # Get list of ordinal borders, and if the country is in the database
    borderList, line_count = borders(country)
    ordinalBorderList, existance = borderOfBorders([country], line_count, borderList)

    # Temporary fix for tertiary
    if (ordinalValue == 3):
        tertiaryBorderList, existance = borderOfBorders(
            [country]+borderList, line_count, ordinalBorderList)

    # If country wasn't found in the database
    if (not existance):
        return NOT_IN_DATABASE_ORDINAL
    
    # If country was in database, but has no ordinal borders
    if (len(ordinalBorderList) == 0):
        if (ordinalValue == 2):
            return country + NO_ORDINAL_BORDERS
        else: 
            return country + NO_TERTIARY_BORDERS + stringifyList(tertiaryBorderList)
    
    # If country was in database, and has one ordinal border
    elif (len(ordinalBorderList) == 1):
        if (ordinalValue == 2):
            return country + ONE_ORDINAL_BORDERS + stringifyList(ordinalBorderList)
        else:
            return country + ONE_TERTIARY_BORDERS + stringifyList(tertiaryBorderList)
    
    # If country was in database, and has multiple ordinal borders
    if (ordinalValue == 2):
        return country + MULTIPLE_ORDINAL_BORDERS + stringifyList(ordinalBorderList)
    else: 
        return country + MULTIPLE_TERTIARY_BORDERS + stringifyList(tertiaryBorderList)