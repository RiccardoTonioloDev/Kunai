import string

def count_words(text,letters):
    Words = {}
    
    for letter in text:
        if letter not in string.ascii_letters:
            text = text.replace(letter , " ")
    
    for word in text.split():
        if word in Words:
            Words[word] += 1
        elif len(word) == letters:
            Words[word] = 1
            
    Words = dict(sorted(Words.items() , key= lambda item:item[1], reverse= True))
    return Words

# USAGE 
print(count_words("Hello World" , 5))





