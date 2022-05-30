

from operator import truediv


def command(token, splitter, string):
    if token not in string: return None
    start = string.index(token) + len(token)

    if (len(splitter) > 1):
        pass # using a regex as the splitter so need to check if one of the chars in is present and stop the string at that point
    elif(len(splitter) < 1):
        return string[start:]
    elif (len(splitter) == 1):
        return string[start:].split(splitter)[0]




def check(token, string):
    if (string.index(token) == 0): return True
    return False
