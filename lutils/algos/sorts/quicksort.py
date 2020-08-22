# Time complexity: O(n*log(n))
# Space complexity: O(log(n))
# Here to illustrate Quick Sort algorithm
def partition(arr, start, end):
    """Moving elements to left and right to pivot to make sure arr[pi] is at the right position
Input: 
    - arr: array to be sorted
    - start: start position/index
    - end: end position/index
Return: pi"""
    # ----_small-----start--------------------end-----------
    #----------------a[i]-------small---------a[i]----end--
    #----------------a[i]-------end(pivot)----a[i]---------
    # Return _small = positiion of Pivot = new position of end value
    _pi = arr[end] #pivot as last element
    _small = start - 1 # smaller index indicator (=0 at the start)
    for i in range(start, end):
        # run a loop for a whole array
        if arr[i] <= _pi:
            # Increase the index (room) for smaller value
            _small = _small+1
            # moving smaller values to the left by swapping
            arr[_small], arr[i] = arr[i], arr[_small]
    # Finally, moving elemet with pivot value (last one) to the middle (end of smaller)
    _small = _small+1
    arr[_small], arr[end] = arr[end], arr[_small]
    # return value
    return _small

def quickSort(arr, start, end):
    """Sort by Quick Sort Alg
Input: 
    - arr: array to be sorted
    - start: start position/index
    - end: end position/index
Return: None    
This quick sort will get last element value as pivot"""
    if start < end:
        # there're more than 1 element in the arr
        pipos = partition(arr, start, end)
        # do the sort again with 2 halves
        quickSort(arr, start, pipos-1)
        quickSort(arr, pipos+1, end)

if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    quickSort( testarr, 0, (len(testarr)-1) )
    print(testarr)
    # python .\quicksort.py
    # [10, 7, 8, 9, 1, 5, 11, 22, 33, 1, 2, 3, 6, 7, 8, 22, 55, 66, 77, 56, 67, 78, 98, 89, 99, 87, 78, 77, 55, 54, 53, 56, 5]
    # [1, 1, 2, 3, 5, 5, 6, 7, 7, 8, 8, 9, 10, 11, 22, 22, 33, 53, 54, 55, 55, 56, 56, 66, 67, 77, 77, 78, 78, 87, 89, 98, 99]
    