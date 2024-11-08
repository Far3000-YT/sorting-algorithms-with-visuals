import pygame
from random import shuffle
from typing import Callable, Iterator

#generate random list from 1 to x not in order
numbers = list(range(1, 201))
shuffle(numbers)

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

# pygame functions here
def pyg(funct: Callable[[list], Iterator], num: list):
    pygame.init()

    screen_width, screen_height = max(numbers)*5, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sorting Algorithm Pygame')

    width, height = screen_width // len(num), screen_height
    sorting_gen = funct(num)
    max_value = max(num)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        try:
            cl = next(sorting_gen)
            screen.fill((0, 0, 0))  #black

            for i, value in enumerate(cl):
                scaled_height = (value / max_value) * screen_height
                pygame.draw.rect(screen, (255, 255, 0), (i * width, screen_height - scaled_height, width, scaled_height))
            pygame.display.flip()
        
        except StopIteration:
            pygame.time.wait(10000) #10 sec wait
            break
    
    pygame.quit()


############################################################################################################

#selection sort function
def selection_sort(num: list):
    yield num  #yield the initial state of the list before the sorting starts
    start_index = 0
    index = 1
    min_value = num[start_index]
    #iterate through the list until we hit the last index (so the list will be sorted when that happens)
    while start_index < len(num):
        min_value = min(min_value, num[index])
        if index == len(num) - 1:
            #swap the 2 indexes in the list
            num[num.index(min_value)], num[start_index] = num[start_index], num[num.index(min_value)]

            start_index += 1
            index = start_index

            try:
                min_value = num[start_index]
            except Exception:
                pass #in case we go out of range

        else:
            index += 1

        #yield for each iteration
        yield num

    print(num)


############################################################################################################

x = input("Choice : ")

match x:
    case "1":
        pyg(selection_sort, numbers)  #Pass the function and numbers
    case "2":
        pass
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case _:
        print("Please put a valid input!")