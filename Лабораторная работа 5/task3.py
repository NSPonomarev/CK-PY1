import random


def get_unique_list_numbers() -> list[int]:
    lst = []
    step = 0
    start = -10
    stop = 10
    count = 15
    while step != count:
        i = random.randint(start, stop)
        if i not in lst:
            lst.append(i)
            step += 1
    return lst


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#
