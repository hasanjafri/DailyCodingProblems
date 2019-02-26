def valid_utf8_bytes(utf8_array):
    if len(utf8_array) > 1:
        array_length = len(utf8_array)
        if str(utf8_array[0])[:array_length] != ('1' * array_length):
            return False
        elif str(utf8_array[0])[array_length] != '0':
            return False
        else:
            for byte in utf8_array[1:]:
                if len(str(byte)) != 8:
                    return False
                elif str(byte)[0] != '1':
                    return False
                elif str(byte)[1] != '0':
                    return False
                else:
                    return True
    else:
        if str(utf8_array[0])[0] != 0:
            return False
        elif len(utf8_array[0]) != 8:
            return False
        else:
            return True

if __name__ == "__main__":
    print(valid_utf8_bytes([11100010, 10000010, 10101100]))