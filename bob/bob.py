import re


def hey(what):
    stripped_str = what.strip()
    stripped_str = re.sub('[^\w\ \?]', '', stripped_str, flags=re.U)
    if stripped_str.isupper():
        return "Whoa, chill out!"
    elif stripped_str[-1:] == '?':
        return "Sure."
    if stripped_str == '':
        return 'Fine. Be that way!'
    else:
        return "Whatever."
