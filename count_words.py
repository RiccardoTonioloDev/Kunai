import string


def count_words(text, letters=None):
    # PRE: text is a string; letters eventually is a number
    # POST: it returns a dictionary with the frequencies of all the words in the text.
    # If letters is specified, then the words will be filtered on their length being equal to letters.
    for letter in text:
        if letter not in string.ascii_letters:
            text = text.replace(letter, " ")

    if letters is None:
        Words = text.split()
        wfreq = [Words.count(w) for w in Words]
        return dict(sorted(dict(zip(Words, wfreq)).items(), key=lambda item: item[1], reverse=True))
    else:
        Words = {}
        for word in text.split():
            if word in Words:
                Words[word] += 1
            elif len(word) == letters:
                Words[word] = 1
        return dict(sorted(Words.items(), key=lambda item: item[1], reverse=True))


# USAGE
print(count_words("pronto prova, sa sa, prova microfono, uno due 3"))
print(count_words("pronto prova, sa sa, prova microfono, uno due 3", 3))
