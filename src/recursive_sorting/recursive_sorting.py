# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
 # Create a new, array of length len(arrA) + len(arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Create markers for a and b starting at 0
    a = 0
    b = 0
    # While a and b are less than the length of the arrA and arrB respectively
    for i in range(0, elements):
        # Compare the items at indices a/b, add the smallest to the merged array
        # Increment a/b, whichever was smallest
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:  # arrA[a] >= arrB[b]
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case: if len(arr) is 0 or 1 then return arr
    if len(arr) <= 1:
        return arr
    else:
        # split the list in half and sort each
        arrA = merge_sort(arr[:len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2:])
        # merge sorted halves
        return merge(arrA, arrB)




















# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
