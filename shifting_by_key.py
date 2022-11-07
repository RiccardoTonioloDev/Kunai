def shift_char_by_key(char1, key, startingLetter):
    return chr(((ord(char1)-ord(startingLetter))+(ord(key)-ord(startingLetter))) % 26+ord(startingLetter))


def deshift_char_by_key(char1, key, startingLetter):
    return chr(((ord(char1)-ord(startingLetter))-(ord(key)-ord(startingLetter))) % 26+ord(startingLetter))


# USAGE
print(deshift_char_by_key(shift_char_by_key('c', 'a', 'a'), 'a', 'a'))
print(deshift_char_by_key('c', 'a', 'a'))
