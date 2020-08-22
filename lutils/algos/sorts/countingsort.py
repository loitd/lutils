def countingSort(a1):
    # Time complexity: O(n+k)
    # Space complexity: O(k) - larger max - larger space
    n = len(a1)
    k = max(a1)
    cnt = [0]*(k+1)
    # sorting and couting
    for i in range(n):
        cnt[a1[i]] +=1
    # Start to iter the sorted values
    p = 0
    a2=[0]*n
    for i in range(k+1):
        for j in range(cnt[i]):
            a2[p]=i
            p+=1     
               
a2 = countingSort([3,1,2,9,0])