def replace_char_by_list(text, tuplesForSubstituitions):
    for tupl in tuplesForSubstituitions:
        # for each tuple of substitution it replaces the first element with the second
        # inside of text
        text = text.replace(tupl[0], tupl[1])
    return text


# USAGE
print(replace_char_by_list("A'I MFFG", [
      ('A', 'i'),
      ('I', 'm'),
      ('M', 'g'),
      ('F', 'o'),
      ('G', 'd')
      ]))
