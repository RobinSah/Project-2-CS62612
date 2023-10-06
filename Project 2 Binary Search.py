from timeit import default_timer as timer
import random
start = timer() #Calculates the starting of execution time

def bin_search(A, x):
    """
    A binary search program to search for a specific element with time complexity 
    O (log n)"""
    l = 0
    h = len(A) - 1
    
    while l <= h:
        mid = (l + h) // 2
        if A[mid] == x:
            return mid #Element found
        elif A[mid] < x:
            l = mid + 1  #Search the right half by setting low to mid + 1
        else:
            h = mid - 1  #Search the left half for the element
    return -1  #Element not found

n = 100
A = sorted([random.randint(1, 100) for _ in range(n)])
x = random.randint(1, 100)
index = bin_search(A, x)

end = timer()   #Calculates the end time of execution time
print(end - start)