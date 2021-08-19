# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Takes input from terminal, with two countries seperated by a comma.
# Returns Yes or No depending on if the countries border each other

import sys

from utils import removeUnwantedChars
from borderingCountries import borders
from ordinalBorderingCountries import borderOfBorders
from databaseFunctions import altNames

from Text_Printed.bordersOutput import BORDER_EACH_OTHER, DO_NOT_BORDER_EACH_OTHER, SECONDARY_BORDER_EACH_OTHER, TERTIARY_BORDER_EACH_OTHER, QUATERNARY_BORDER_EACH_OTHER

if __name__ == '__main__':
    # Take two countries seperated by comma from the terminal
    countries = input().split(",")

    # Remove new lines and get official names for countries
    for i, country in enumerate(countries):
        countries[i] = altNames(removeUnwantedChars(countries[i]))

    # Get out the borderlist and ordinal border lists
    borderList, match_count = borders(countries[0])
    ordinalBorderList, exists = borderOfBorders([countries[0]], match_count, borderList)

    # Temporary bodge
    tertiaryBorderList, exists = borderOfBorders([countries[0]]+borderList, match_count, ordinalBorderList)
    quaternaryBorderList, exists = borderOfBorders([countries[0]]+borderList+ordinalBorderList, match_count, tertiaryBorderList)

    # If second country borders the first country
    if (countries[1] in borderList):
        print(BORDER_EACH_OTHER.format(c1 = countries[0], c2 = countries[1]))
    
    # If second country is seperated by one
    elif (countries[1] in ordinalBorderList):
        print(SECONDARY_BORDER_EACH_OTHER.format(c1 = countries[0], c2 = countries[1]))

    # If second country is seperated by two (TEMP)
    elif (countries[1] in tertiaryBorderList):
        print(TERTIARY_BORDER_EACH_OTHER.format(c1 = countries[0], c2 = countries[1]))
    
    # If second country is seperated by three (TEMP)
    elif (countries[1] in quaternaryBorderList):
        print(QUATERNARY_BORDER_EACH_OTHER.format(c1 = countries[0], c2 = countries[1]))
    
    # If second country is two or more degrees of seperation away, or can never border
    else:
        print(DO_NOT_BORDER_EACH_OTHER.format(c1 = countries[0], c2 = countries[1]))