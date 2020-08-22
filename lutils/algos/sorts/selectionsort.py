# https://www.programiz.com/dsa/selection-sort
def selectionSort(a1):
    # Time complexity: O(n^2)
    # Space complexity: O(1) - use 1 temp var
    n=len(a1)
    for i in range(n-1):
        mini = i
        # find the lowest
        for j in range(i+1,n):
            if a1[j] < a1[mini]:
                mini = j #only assign when lower
                # lowest after finish the inner loop
        # switch with first element
        a1[i],a1[mini]=a1[mini],a1[i]

# selectionSort(a1)

if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    selectionSort( testarr )
    print(testarr)
            