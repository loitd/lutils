# Here to illustrate Bubble Sort algorithm
# Bubble Sort sort by switching positions
def bubbleSort(arr):
    # We'll do len(arr) factorial = n! scan/loop times
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            # the arr will be sort from RIGHT to LEFT, the bigger is at the RIGHT
            if arr[j] > arr[j+1]:
                # Do swapping
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    bubbleSort( testarr )
    print(testarr)