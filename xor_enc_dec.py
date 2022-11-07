# Funziona ma non esattamente.
def xor_enc_dec(data, key):
    newKey = []
    for idx in range(len(data)):
        newKey.insert(0, key[idx % len(key)])
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(data, key)])


# USAGE
print(xor_enc_dec(xor_enc_dec("ciao menny", "hello"), "hello"))
