def to_hex(string):
    output = ""
    for char in string:
        output += hex(ord(char)).split('0x')[1]
    return output


def hash_function(string):
    # TODO Use a secure hash
    return to_hex(string)
