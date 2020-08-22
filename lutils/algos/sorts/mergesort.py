# https://www.programiz.com/dsa/merge-sort
def mergeSort(a1):
    # Time complexity: O(n*log(n))
    # Space complexity: O(n)
    n = len(a1)
    if n>1:
        mid = n//2
        rig = a1[:mid]
        lef = a1[mid:]
        
        # recursive
        mergeSort(rig)
        mergeSort(lef)
        # finish this step, all a1 has been splitted to single elements
        
        i=k=j=0
        # now sort and merge back
        while i<len(lef) and j<len(rig):
            if lef[i] < rig[j]:
                a1[k] = lef[i]
                i +=1
            else:
                a1[k] = rig[j]
                j+=1
            k+=1
        
        # collect everything left
        while i<len(lef):
            a1[k] = lef[i]
            i+=1
            k+=1
        while j<len(rig):
            a1[k] = rig[j]
            j+=1
            k+=1


if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    mergeSort( testarr )
    print(testarr)