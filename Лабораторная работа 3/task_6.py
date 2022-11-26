list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max = 0
value_max = list_numbers[index_max]

for i, value_current in enumerate(list_numbers):
    if value_current >= value_max:
        index_max = i
        value_max = list_numbers[index_max]

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)

