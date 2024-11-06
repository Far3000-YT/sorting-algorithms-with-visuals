import random

#generate random list from 1 to 1000 not in order
numbers = list(range(1, 11))
random.shuffle(numbers)

#base text for input
print("""
WELCOME ! Choose the sorting algorithm you want to see : 
    [1] - SELECTION SORT
    [2] - INSERTION SORT
    [3] - BINARY INSERTION SORT
    [4] - MERGE SORT
    [5] - QUICK SORT (LR ptrs)
""")


############################################################################################################


#algorithms start (no explanation on how they work it's too long)
def selection_sort(numbers: list):
    start_index = 0
    index = 1
    min_value = numbers[0]
    #iterate through the list until we hit the last index (so the list will be sorted when that happens)
    while start_index != len(numbers) - 1:
        min_value = min(min_value, numbers[index])
        if index == len(numbers) - 1:
            new_val = numbers[numbers.index(min_value)]
            numbers[start_index], numbers[numbers.index(min_value)] = numbers[numbers.index(min_value)], numbers[start_index]
            start_index += 1
            index = start_index
        else:
            index += 1
        print(numbers)


############################################################################################################


x = input("Choice : ")

match x:
    case "1":
        selection_sort(numbers)
    case "2":
        print("2")
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case _:
        print("Please put a valid input !")