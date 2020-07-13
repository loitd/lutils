# https://medium.com/tuanbinhblog/8-thu%E1%BA%ADt-to%C3%A1n-s%E1%BA%AFp-x%E1%BA%BFp-ph%E1%BB%95-bi%E1%BA%BFn-trong-java-2c39de4272ce
# Ý tưởng thuật toán selection sort là: Chọn phần tử nhỏ nhất trong n phần tử ban đầu, đưa phần tử này về vị trí đúng là đầu tiên của dãy hiện hành. 
# Sau đó không quan tâm đến nó nữa, xem dãy hiện hành chỉ còn n-1 phần tử của dãy ban đầu, bắt đầu từ vị trí thứ 2. Lặp lại quá trình trên cho dãy hiện hành đến khi dãy hiện hành chỉ còn 1 phần tử. 
# Dãy ban đầu có n phần tử, vậy tóm tắt ý tưởng thuật toán là thực hiện n-1 lượt việc đưa phần tử nhỏ nhất trong dãy hiện hành về vị trí đúng ở đầu dãy.

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                # switch
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    testarr = [10, 7, 8, 9, 1, 5,11,22,33,1,2,3,6,7,8,22,55,66,77,56,67,78,98,89,99,87,78,77,55,54,53,56,5]
    print(testarr)
    selectionSort( testarr )
    print(testarr)
            