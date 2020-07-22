# # TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arr, p, q, r):

#     # make copies of sub arrays to be sorted
#     l = arr[p:q]
#     m = arr[q+1:p]
#     n1 = q - p + 1
#     n2 = r - q
#     for i in range(0, n1):
#         l[i] = arr[p + i]
#     for j in range(0, n2):
#         m[j] = arr[q + 1 + j]
    
#     # keep track of the current 
#     # index of the sub arrays
#     i = 0
#     j = 0
#     k = p


#     while i < n1 and j < n2:
#         if l[i] <= m[j]:
#             arr[k] = l[i]
#             i += 1
#         else:
#             arr[k] = m[j]
#             j += 1
#         k += 1
    
#     while i < n1:
#         arr[k] = l[j]
#         i += 1
#         k += 1
    
#     while j < n2:
#         arr[k] = m[j]
#         j += 1
#         k += 1


# # TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr, p, r):
#     # Exit Critera?
#     # we are tyring to preform a mergesort onto a subarray of size 1
#     if p >= r:
#         return

#     # Working to exit critera?
#     # Solve for the mid index
#     q = (p + r) // 2
#     # Call self with the first half
#     merge_sort(arr, p, q)
#     # Call self with the second half
#     merge_sort(arr, q+1, r)
#     # Merge!
#     merge(arr, p, q, r)

#     return arr

# reimplementation
def merge_sort(array):
    # if we have'nt yet been reudced
    # down passed a s single array
    if len(array) > 1:
        # our midpoint
        r = len(array)//2
        # first half
        L = array[:r]
        # second half
        M = array[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)

        
        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

