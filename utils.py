def stringifyList(list):
    string = ""
    
    for item in list:
        string += item + ", "

    return string[:-2]

def removeNewLine(string):
    # If string has new line at the end, remove it
    if (string[-1] == '\n'):
        return string[:-1]
    return string