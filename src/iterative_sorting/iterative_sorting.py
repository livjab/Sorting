# TO-DO: Complete the selection_sort() function below
#
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # Loop through elements on right-hand-side of current index
        for j in range(cur_index, len(arr)):
            # Find next smallest element
            if arr[j] < arr[smallest_index]:
                # Assign to smallest_index
                smallest_index = j

        # Swap the element at current index with the smallest element found in above loop
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

  swap_occured = True

  while swap_occured:
    # set to false to stop loop if no swap occurs
    swap_occured = False
    
    # Loop through array
    for i in range(0, len(arr)-1):
      current = i
      neighbor = i+1

      # compare each element to its neighbor
      if arr[current] > arr[neighbor]:
        # If elements in wrong positions, swap them
        arr[current], arr[neighbor] = arr[neighbor], arr[current]
        # If swap occurs, change boolean
        swap_occured = True

    # If no swaps performed, stop. Else go back to beginning and repeat.

  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
