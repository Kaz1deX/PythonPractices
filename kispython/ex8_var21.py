import re


def main(string):
    pattern = r"\[\s*([-\d]+)\s*to\sq\((\w+)\)"
    matches = re.findall(pattern, string)
    pairs = [(match[1], match[0]) for match in matches]
    dictionary = dict(pairs)
    for key in dictionary:
        dictionary[key] = int(dictionary[key])
    return dictionary
