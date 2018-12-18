def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(n=i):
            print(n)
        flist.append(print_i)

    return flist

if __name__ == '__main__':
    funcs = make_functions()
    for f in funcs:
        f()
    