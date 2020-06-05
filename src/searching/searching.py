def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1  # not found

    low = 0
    high = len(arr) - 1

    while low <= high:
        #go to the middle
        middle = low + (high - low) // 2

        #ask if the middle is less than or greater than our target
        ##if less, eliminate the right-hand side

        if target < arr[middle]:
            high = middle - 1
        
        elif target > arr[middle]:
            low = middle + 1
        
        else:
            return middle

    return -1


    # Classmates code -- from lecture
    # right = len(arr) - 1 
    # left = 0
    
    # while True:
    #     middle = (left+ right)//2
    #     if left > right or len(arr) == 0:
    #         return -1
    #     elif arr[middle] == target:
    #         return middle
    #     elif target < arr[middle]:
    #         right = middle - 1
    #     elif target > arr[middle]:
    #         left = middle + 1
    #     else: 
    #         return middle
    # return -1  # not found

    #Classmate #2 code in class
# def binary_search(arr, target):
#     # if there are no items in the array we return false for target found
#     if len(arr) == 0:
#         return -1  # not found
#     # variables to hold index values for bisection of binary search
#         low = 0
#         high = len(arr) - 1

#         while low <= high:
#             middle = low + (high - low) // 2
#             if arr[middle] == target:
#                 return middle
#             elif arr[middle] > target:
#                 high = middle - 1
#             else:
#                 low = middle + 1
#         return -1