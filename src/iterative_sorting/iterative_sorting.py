# TO-DO: Complete the selection_sort() function below
# Notes:
# Types of sort -- selection sort, insertion sort and bubble sort
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        for j in range(cur_index + 1, len(arr)): #don't have to start at the absolute start of current index -- can do one after, the range is "from the first thing after the current index through the length of the array"
            #compare all these values to the value at cur_index
            #find the smallest
            if arr[j] < arr[smallest_index]:
                smallest_index = j #this finds the smallest index and now we need to swap them out
        
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        #Sidenote -- this python structure works because of destructuring -- if you return multiple items, python wraps that in a tool. 
        #So on the the left of the = it is unpacking and assigning, on the right it is a tuple.

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    made_a_swap = True #starts the while loop
    #iterate over two arrays and compare two pointers and swap them if true
    while made_a_swap: #ideal situation we don't need to do the swap so made_a_swap is false
        made_a_swap = False
    #otherwise, we do the following
        for i in range(0, len(arr) - 1):
            j = i + 1

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                made_a_swap = True
    
    return arr

    #Classmate's neat version
    # def bubble_sort(arr):
    # # Set incoming array to a variable for DRY code
    # init = range(len(arr) - 1)
    # # Tells second loop where to start at, runs for each value in the list
    # for i in init:
    #     # Starts at 0
    #     for j in init:
    #         # Compare values
    #         if arr[j] > arr[j+1]:
    #             # Perform the swap
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    counts = [0] * (maximum + 1)

    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[value] += 1
    
    j = 0
    for i in range(0, len(counts)):
        while counts[i] > 0:
            arr[j] = i
            j += 1
            counts[i] -= 1

    return arr

