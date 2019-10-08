# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
   # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        
        for smallest_index in range(i, len(arr)):
            if arr[cur_index] > arr[smallest_index]:
                cur_index = smallest_index

        # TO-DO: swap
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)-1, 0, -1):
       for x in range(i):
           if arr[x] > arr[x + 1]:
               arr[x], arr[x + 1] = arr[x + 1], arr[x]
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr