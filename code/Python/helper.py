import math


def command(token, splitter, string):
    #if token not in string: return None
    start = string.index(token) + len(token)

    end = len(string)
    for i in range(len(splitter)):
        try:
            temp = string[start:].index(splitter[i])
            if (temp < end): end = temp                                             
        except:
            pass
    return string[start:end + start]


def check(token, string):
    try:   
        if (string.index(token) == 0): return True
        return False
    except:
        return False


def dist(a, b): # only works with objects that have an x and y variable
    return math.sqrt(math.pow(a.x - b.x) + math.pow(a.y - b.y))
