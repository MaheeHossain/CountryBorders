import sys

from utils import removeNewLine
from borderingCountries import bordersOutput
from ordinalBorderingCountries import ordinalBordersOutput
from readFiles import readInput
from Text_Printed.errorMessages import ORDINAL_AMOUNT_TOO_LOW

if __name__ == '__main__':
    fptr = sys.stdout

    countries = readInput()
    ordinalValue = int(countries[0])
    if (ordinalValue > 0):
        for country in countries[1:]:
            result = bordersOutput(removeNewLine(country))
            fptr.write(result + '\n')
            if (ordinalValue > 1):
                ordinalResult = ordinalBordersOutput(removeNewLine(country))
                fptr.write(ordinalResult + '\n' + '\n')
    else:
        print(ORDINAL_AMOUNT_TOO_LOW)

    fptr.close()