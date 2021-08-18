import sys

from utils import removeNewLine
from borderingCountries import bordersOutput, secondaryBordersOutput
from readFiles import readInput

if __name__ == '__main__':
    fptr = sys.stdout

    countries = readInput()
    for country in countries:
        result = bordersOutput(removeNewLine(country))
        fptr.write(result + '\n')
        secondResult = secondaryBordersOutput(removeNewLine(country))
        fptr.write(secondResult + '\n' + '\n')


    fptr.close()