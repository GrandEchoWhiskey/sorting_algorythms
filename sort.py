from sorting import quicksort, mergesort, bubblesort, selectionsort
import random
from copy import deepcopy
from time import thread_time

class timer:
    def __init__(self):
        self.start = thread_time()
    def stop(self):
        return thread_time() - self.start

rand_list = random.choices(range(1000), k=100)
sorted_list = [n for n in range(0, 100)]
reversed_list = [n for n in range(100, 0)]

def main():
    print(rand_list)
    print(quicksort(deepcopy(rand_list)))

if __name__ == "__main__":
    main()