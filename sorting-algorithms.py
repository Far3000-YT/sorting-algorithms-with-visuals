import random

#generate random list from 1 to x not in order
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


#algorithms start
def selection_sort(num: list):
    print(num)
    start_index = 0
    index = 1
    min_value = numbers[start_index]
    #iterate through the list until we hit the last index (so the list will be sorted when that happens)
    while start_index < len(num):
        min_value = min(min_value, num[index])
        if index == len(num) - 1:            
            #swap the 2 indexes in the list
            num[num.index(min_value)], num[start_index] = num[start_index], num[num.index(min_value)]

            start_index += 1
            index = start_index
            
            try: min_value = num[start_index]
            except Exception: pass #bcs we will go out of range and i dont want to debut this

        else:
            index += 1

    print(num)



############################################################################################################


x = input("Choice : ")

match x:
    case "1":
        selection_sort(numbers)
    case "2":
        pass
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case _:
        print("Please put a valid input !")