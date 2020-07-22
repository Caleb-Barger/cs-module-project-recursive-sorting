# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, high, low):
    # Exit Critera?
    if low <= high:
        return -1

    # Getting twords an exit critera?

    # 1) calculate middle of array
    mid = (high + low) // 2
    # if the middle of our array is the target than great
    if target == arr[mid]:
        return mid

    # 2) if the target is less than the array[mid]
    if target < arr[mid]:
        # cut out the right half
        high = mid - 1
        # high is now mid - 1
        return binary_search(arr, target, high, low)

    # 3) if the target is greater than our array[mid]
    if target > arr[mid]:
        # cut out the left side
        low = mid + 1
        # reasign low to mid + 1
        return binary_search(arr, target, high, low)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

