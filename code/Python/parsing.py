

def command(token, splitter, string):
    if token not in string: return None

    start = string.index(token) + len(token)

    return string[start:].split(splitter)[0]