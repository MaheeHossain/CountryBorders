# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions to help deal with files

INPUT_FILE = './Test_cases/Input.txt'

def readInput():
    # Reads the input file and returns an array with all countries
    lines=[]
    with open(INPUT_FILE) as f:
        lines = f.readlines()
    return lines