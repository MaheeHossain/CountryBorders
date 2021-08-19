# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions to help deal with files

INPUT_FILE = './Test_cases/Input.txt'
ALT_NAMES = './Test_cases/alternativeNames.txt'

def readInput():
    # Reads the input file and returns an array with all countries
    lines=[]
    with open(ALT_NAMES) as f:
        lines = f.readlines()
    return lines