import pygame
from random import shuffle
from typing import Callable, Iterator

#generate random list from 1 to x in order then shuffle them to make them not in order
maxi = 201
numbers = list(range(1, maxi))
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
def pyg(funct: Callable[[list], Iterator], num: list): #gpt for this line (the callable)
    pygame.init()

    screen_width, screen_height = maxi*5, maxi*2
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sorting Algorithms With Visuals')

    width, height = screen_width // len(num), screen_height
    sorting_gen = funct(num)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        try:
            cl = next(sorting_gen)
            screen.fill((0, 0, 0)) #black

            for i, value in enumerate(cl):
                scaled_height = (value / maxi) * screen_height
                pygame.draw.rect(screen, (255, 255, 140), (i * width, screen_height - scaled_height, width, scaled_height))
            pygame.display.flip()

            pygame.time.wait(50)
        
        except StopIteration:
            pygame.time.wait(5000) #10 sec wait
            break
    
    pygame.quit()


############################################################################################################

#selection sort function
def selection_sort(num: list):
    yield num #yield the initial state of the list before the sorting starts
        
    for start_index in range(len(num) - 1):
        min_index = start_index
        
        #find the minimum value
        for index in range(start_index + 1, len(num)):
            if num[index] < num[min_index]:
                min_index = index

        #swap the 2 indexes in the list
        if min_index != start_index:
            num[start_index], num[min_index] = num[min_index], num[start_index]

        #yield for each iteration
        yield num


############################################################################################################


#insertion sort
def insertion_sort(num: list):
    yield num

    for s in range(1, len(num)):
        selected_val = num[s]
        min_one = s - 1

        while min_one >= 0 and selected_val < num[min_one]:
            num[min_one + 1] = num[min_one]
            min_one -= 1
        
        num[min_one + 1] = selected_val
        yield num


############################################################################################################


x = input("Input : ")

match x:
    case "1":
        pyg(selection_sort, numbers)
    case "2":
        pyg(insertion_sort, numbers)
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case _:
        print("Please put a valid input!! :(")