import random

#generate random list from 1 to 1000 not in order
numbers = list(range(1, 1001))
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
    index = 1
    #iterate through the list comparing value and value-1 index, if value-1 is smaller then its good otherwise we reset
    while index != len(numbers) - 1:
        if numbers[index-1] <= numbers[index]:
            pass


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