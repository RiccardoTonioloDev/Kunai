# THE KEY IS A STRING
def xor_enc_strk(data, key):
    # PRE: data is a string; key is a string
    # POST: it's returned an array of binaries in hex form
    newKey = []
    for idx in range(len(data)):
        newKey.insert(0, key[idx % len(key)])
    return [chr(ord(x) ^ ord(y)) for x, y in zip(data, newKey)]


def xor_dec_strk(data, key):
    # PRE: data it's an array of binaries in hex form; key is a string
    # POST: it's returned a decrypted string (it's the right string, only if the right
    # key is used)
    newKey = []
    for idx in range(len(data)):
        newKey.insert(0, key[idx % len(key)])
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(data, newKey)])


# THE KEY IS AN INTEGER/CHAR


def xor_enc_intk(data, key):
    # PRE: data is a string; key is an integer
    # POST: it's returned an array of binaries in hex form
    newKey = []
    for idx in range(len(data)):
        newKey.insert(0, key)
    return [chr(ord(x) ^ y) for x, y in zip(data, newKey)]


def xor_dec_intk(data, key):
    # PRE: data it's an array of binaries in hex form; key is an integer
    # POST: it's returned a decrypted string (it's the right string, only if the right
    # key is used)
    newKey = []
    for idx in range(len(data)):
        newKey.insert(0, key)
    return ''.join([chr(ord(x) ^ y) for x, y in zip(data, newKey)])


# USAGE
print(xor_dec_strk(xor_enc_strk('c', "un carattere"), "un carattere"))
print(xor_dec_strk(xor_enc_strk("ciao menny", "hello"), "hello"))
print(xor_dec_intk(xor_enc_intk("ciao carra", 150), 150))
