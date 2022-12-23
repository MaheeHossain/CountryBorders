# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions to help deal with files

def readInput(file):
    # Reads the input file and returns an array with all countries
    lines=[]
    with open(file) as f:
        lines = f.readlines()
    return lines