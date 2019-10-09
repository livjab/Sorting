# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge_helper( a, b ):

  merged_arr = []

  # starting at beginning of `a` and `b`
  a_index = 0
  b_index = 0

  elements = len(a) + len(b)

  while len(merged_arr) < elements:

      a_start = a[a_index]
      b_start = b[b_index]
      #print(a_start, b_start)

      # compare the next value of each list

      if a_start < b_start:
        # add smallest to `merged_arr`
        merged_arr.append(a_start)

        # increment a_start by 1
        a_index += 1

      else:
        # add smallest to `merged_arr`
        merged_arr.append(b_start)

        # increment b_start by 1
        b_index += 1


      if a_index == len(a):
          # Reached the end of a
          # Append the remainder of b and break
          merged_arr += b[b_index:]
          break

      elif b_index == len(b):
          # Reached the end of b
          # Append the remainder of a and break
          merged_arr += a[a_index:]
          break

      #print(merged_arr)

  return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) <= 1:
      return arr

    else:

      LHS = arr[:len(arr)//2]
      RHS = arr[len(arr)//2:]

      # recursively call merge_sort() on LHS
      # recursively call merge_sort() on RHS
      arr = merge_helper(merge_sort(LHS), merge_sort(RHS))


      return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
