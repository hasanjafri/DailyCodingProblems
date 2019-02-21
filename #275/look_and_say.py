from itertools import groupby

string_num = '1'

def look_and_say(N):
    return ''.join(str(len(list(g))) + k for k, g in groupby(N))

if __name__ == "__main__":
    for i in range(6):
        print(string_num)
        string_num = look_and_say(string_num)
