import sys

from utils import removeNewLine
from borderingCountries import bordersOutput
from readFiles import readInput

if __name__ == '__main__':
    fptr = sys.stdout

    countries = readInput()
    for country in countries:
        result = bordersOutput(removeNewLine(country))
        fptr.write(result + '\n')

    fptr.close()