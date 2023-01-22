import random

def random_not_in_list(n, l):
    # Find the set of numbers that are not in the list
    not_in_list = set(range(n)) - set(l)
    # If there are no numbers not in the list, return None
    if not not_in_list:
        return None
    # Otherwise, choose a random number from the set of numbers not in the list
    return random.choice(list(not_in_list))

n = 10
l = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(random_not_in_list(n, l))
