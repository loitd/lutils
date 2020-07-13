# https://medium.com/tuanbinhblog/8-thu%E1%BA%ADt-to%C3%A1n-s%E1%BA%AFp-x%E1%BA%BFp-ph%E1%BB%95-bi%E1%BA%BFn-trong-java-2c39de4272ce
# https://miro.medium.com/max/500/1*k5EJ5ZWXgxDSLjsLQKjmvA.png
# https://www.educative.io/edpresso/merge-sort-in-python

def mergeSort(arr):
    """Implement Merge Sort in Python"""
    if len(arr) > 1:
        # Split to 2 halves
        _mid = len(arr)//2
        _left = arr[:_mid]
        _right = arr[_mid:]
        
        # recursive for _left and _right
        mergeSort(_left)
        mergeSort(_right)
        
        # Init counter
        i,j,k = 0,0,0
        
        while i < len(_left) and j < len(_right):
            if _left[i] < _right[j]:
                # use smaller one
                arr[k] = _left[i]
                i += 1
                k += 1
            else:
                arr[k] = _right[j]
                j += 1
                k += 1
        
        # For all remaining value, move to the end
        while i < len(_left):
            arr[k] = _left[i]
            i += 1
            k += 1
        
        # For all remaining value, move to the end
        while j < len(_right):
            arr[k] = _right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    mergeSort( testarr )
    print(testarr)