from functools import reduce


def add_subtract(x):
    def add_subtract_recursive(x, add_subtract_func):
        def curried_add_subtract(y):
            return add_subtract_func(x, y)
        return curried_add_subtract

    def add_subtract_func(x, y):
        def add_subtract_iterate(acc, item):
            if acc % 2 == 0:
                return acc + item
            else:
                return acc - item

        return reduce(add_subtract_iterate, (x, y), 0)

    return add_subtract_recursive(x, add_subtract_func)


if __name__ == '__main__':
    result = add_subtract(7)
    print(result)
    print(add_subtract(1)(2)(3))
    print(add_subtract(-5)(10)(3)(9))
