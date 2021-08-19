# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Functions that make use of databases

from Borders_database.altNamesDictionary import altNamesDict

def altNames(country):
    # If country inputted is in altnames database, return proper name
    if (country in altNamesDict):
        return altNamesDict[country]
    return country