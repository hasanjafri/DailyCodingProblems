from math import modf, ceil

def first_nonworking_attempt(columnid):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mult, remainder = modf((columnid / 26))
    print(mult, remainder)
    mult = ceil((mult * 26))
    print(mult)
    if mult != 0:
        mult = int(modf(mult)[1]) - 1
    print(mult)
    return "" + (alphabets[mult] * int(remainder+1))


def second_nonworking_attempt(cid):
    mult = 1
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if cid <= 26:
        return alphabets[cid-1]
    else:
        mult = mult + 1
        print(mult)
        return (second_nonworking_attempt((cid - 26))) * mult


def get_alphabetical_column_id(cid):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mult = 1
    while cid > 26:
        mult += 1
        cid -= 26

    return (alphabets[cid-1] * mult)
        


if __name__ == "__main__":
    print(get_alphabetical_column_id(1))
    print(get_alphabetical_column_id(27))
    print(get_alphabetical_column_id(67))