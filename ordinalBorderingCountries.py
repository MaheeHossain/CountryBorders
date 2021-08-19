from utils import stringifyList
from borderingCountries import borders

from Text_Printed.errorMessages import BORDERING_COUNTRY_NO_DATA
from Text_Printed.bordersOutput import NO_SECOND_BORDERS, ONE_SECOND_BORDERS, MULTIPLE_SECOND_BORDERS

def borderOfBorders(originalCountries, lines, country_list):
    # Returns list of countries which border the bordering countries
    # Can make this work for all numbers, not just 2
    ordinalRankBorders = []
    if (lines == 0):
        return ordinalRankBorders
    for country in country_list:
        borderList, line_count = borders(country)
        if (line_count == 0):
            print(BORDERING_COUNTRY_NO_DATA)
        for ordinalCountry in borderList:
            if ((ordinalCountry not in ordinalRankBorders)
             and ordinalCountry not in originalCountries):
                ordinalRankBorders.append(ordinalCountry)
    return ordinalRankBorders

def ordinalBordersOutput(country):
    # Returns the secondary borders with the required strings
    borderList, line_count = borders(country)
    ordinalBorderList = borderOfBorders([country], line_count, borderList)
    if (len(ordinalBorderList) == 0):
        return country + NO_SECOND_BORDERS
    elif (len(ordinalBorderList) == 1):
        return country + ONE_SECOND_BORDERS + stringifyList(ordinalBorderList)
    return country + MULTIPLE_SECOND_BORDERS + stringifyList(ordinalBorderList)