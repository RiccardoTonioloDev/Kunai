def replace_char_by_list(text, tuplesForSubstituitions):
    array_of_switched_chars = []
    for idx, tupl in enumerate(tuplesForSubstituitions):
        # Here it makes sure that we are replacing different chars with the same solution
        if (tupl[1] not in array_of_switched_chars):
            # for each tuple of substitution it replaces the first element with the second
            # inside of text
            text = text.replace(tupl[0], tupl[1])
            array_of_switched_chars.append(tupl[1])
        else:
            print(
                'WARNING: you are trying to replace more than one char with: ', tupl[1])

    return text


# USAGE
print(replace_char_by_list("A'I MFFG", [
      ('A', 'i'),
      ('I', 'm'),
      ('M', 'g'),
      ('F', 'o'),
      ('G', 'd')
      ]))
