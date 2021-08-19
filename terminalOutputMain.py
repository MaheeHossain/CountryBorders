# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Takes input from an input.txt file, with a level of ordinance and a list 
# of countries. The level of ordinance is how many levels of borders you want.
# Level of Ordinance == 1 -> Countries which border country A
# Level of Ordinance == 2 -> Countries which border ordinance 1 countries
# Level of Ordinance == 3 -> Countries which border ordinance 2 countries
# and so on. Returns the each of the ordinances below the one specified. 

import sys

from utils import removeNewLine
from borderingCountries import bordersOutput
from ordinalBorderingCountries import ordinalBordersOutput
from readFiles import readInput
from databaseFunctions import altNames
from Text_Printed.errorMessages import ORDINAL_AMOUNT_TOO_LOW, ORDINANCE_ZERO
from Text_Printed.bordersOutput import NOT_IN_DATABASE_ORDINAL

if __name__ == '__main__':
    fptr = sys.stdout

    # Get list of countries and level of ordinance
    countries = readInput()
    ordinalValue = int(countries[0])

    # If ordinance is a positive number, return borders
    if (ordinalValue > 0):
        for country in countries[1:]:
            # Removes newline from input
            country = altNames(removeNewLine(country))
            result = bordersOutput(country)
            fptr.write('\n' + result + '\n')

            # If ordinance is above one, return borders of borders, to the 
            # degree specified by the ordinance value
            if (ordinalValue > 1):
                ordinalResult = ordinalBordersOutput(country)
                if (ordinalResult == NOT_IN_DATABASE_ORDINAL):
                    fptr.write("")
                else:
                    fptr.write(ordinalResult + '\n')

    # If ordinance value is 0, return the country itself
    elif (ordinalValue == 0):
        print(ORDINANCE_ZERO)
        for country in countries[1:]:
            fptr.write(removeNewLine(country) + " is " + removeNewLine(country) + "\n")
    
    # Ordinance is not a positive number - impossible
    else:
        print(ORDINAL_AMOUNT_TOO_LOW)

    fptr.write('\n')
    fptr.close()