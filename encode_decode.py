import base64


def base64_to_text(b64txt):
    return base64.b64decode(b64txt).decode('UTF-8', errors="ingore")


def text_to_base64(text):
    return base64.b64encode(bytes(text, 'utf-8'))


def text_to_hex(text):
    return text.encode("utf-8").hex()


def hex_to_text(hextxt):
    return bytearray.fromhex(hextxt).decode()


def binaryString_to_text(binaryString):
    tmp = int(binaryString, 2)
    return chr(tmp)


# USAGE
b64txt = text_to_base64("prova 123")
print(b64txt)
print(base64_to_text(b64txt))
hextxt = text_to_hex("ciao a tutti")
print(hextxt)
print(hex_to_text(hextxt))
print(binaryString_to_text('1010011'))  # it's an 'S'
