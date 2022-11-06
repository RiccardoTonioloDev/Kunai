def char_frequency(strToAnalyze):
    dict = {}
    countedChars = 0
    for n in strToAnalyze:
        keys = dict.keys()
        # if a char it's between the range a - Z, or A - Z, then it's counted
        if (ord(n) <= ord('z') and ord(n) >= ord('a')) or (ord(n) <= ord('Z') and ord(n) >= ord('A')):
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
            # here we are keeping a counter, to obtain percentages, for every char counted
            countedChars += 1
    for n in dict:
        # calculating the percentage of relative frequency, for each char counted
        dict[n] = round(dict[n] / countedChars, 2)
    # returning in descending order, to allow a better understanding/readability of the data
    return sorted(dict.items(), key=lambda kv: kv[1], reverse=True)


# USAGE
print(char_frequency("provaprova ciao"))
