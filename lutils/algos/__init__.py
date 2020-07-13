# REF:
# https://viblo.asia/p/tong-hop-thuat-toan-sort-co-ban-vi-du-trong-ngon-ngu-c-Qbq5QqpE5D8

# Tốc độ
# Về tốc độ thì cũng phụ thuộc nhiều vào Machine spec. 　
# Ví dụ, CountingSort thì nhanh nhất 1 cách áp đảo nhưng lại cần có 1 lượng memory không phải "dạng tầm thường" tùy vào phạm vi giá trị. 
# Ngoài ra, đối với Merge sort và Quick sort Thì merge sort nhanh với data nhỏ Quick sort được đánh giá nhanh nhất với data lớn.

# Lượng Memory cần thiết
# Counting Sort > Merge sort > Quick sort > Sellection sort = Odd-even sort = Bubble sort

# 1. Bubble sort
# Bubble sort là 1 thuật toán sort. Đây là phương pháp sort bằng cách vừa so sánh kích cỡ của các yếu tố có phù hợp với phần tử bên cạnh không vừa sắp xếp chúng lại. Xét về thời gian tính toán thì O(n2)O(n2) khá là CHẬM, nhưng do đây là thuật toán ĐƠN GIẢN, cách làm dễ, hơn nữa nó gần với xử lý song song nên thường được sử dụng. Nó được gọi là Sort nội bộ ổn định, hay có các cách gọi khác như Phương pháp exchange cơ bản, Phương pháp trao đổi liền kề.

# bubblesort(N)
#   for i = 0 to N.length-1
#     for j = 0 to N.length-1-i
#       if N[j] < N[j-1]
#         swap N[j] and N[j-1]

# 2. Sellection sort
# Selection sort là 1 thuật toán tìm giá trị lớn nhất hoặc nhỏ nhất từ các phần tử và thay thế với phần tử cuối cùng của dãy. Xét về thời gian tính toán thì O(n2)O(n2) khá là chậm, nhưng do thuật toán đơn giản, cách làm dễ nên thường được sử dụng. Đây không phải là sort ổn định. Đây là thuật toán chọn phần tử nhỏ nhất trong chuỗi, di chuyển nó đến phía bên trái (Cụ thể là vị trí key). Rất dễ hiểu đúng không?

# SelectionSort(A)
# for i = 0 to A.length-1
#   mini = i
#   for j = i to A.length-1
#     if A[j] < A[mini]
#         mini = j
#   swap A[i] and A[mini]

# 4. Merge sort
# Merde sort là 1 thuật toán sort bằng cách, nếu khi merge nhiều phần tử đã được sắp xếp sẵn vào 1 dãy mà sắp xếp theo thứ tự từ nhỏ đến lớn, thì dãy mới cũng được sắp xếp lại. Khi sort các array có chứa data nn phần tử, thì lượng tính toán tệ nhất là O(nlogn)O(nlogn). Thực tế cũng tùy thuộc vào cách làm phân chia hay tích hợp, nhưng thông thường thì có thể sort ổn định. In-place sort cũng được đưa ra, nhưng thường thì cần có lưu trữ bên ngoài O(n)O(n).

# 5. Quick Sort
# Quick sort là thuật toán được phát triển bởi nhà khoa học máy tính Charles Antony Richard Hoare vào năm 1960. Lượng tính toán tốt nhất và tính toán trung bình là O(nlogn)O(nlogn). So với các phương pháp sort khác thì đây được coi là phương pháp nhanh nhất, tuy nhiên không phải do số data hay cách sắp xếp các đối tượng thì sẽ nhanh, lượng tính toán tệ nhất là O(n2)O(n2). Đây không phải là kiểu sort ổn định.

# Partition(A, p, r)
#   x = A[r]
#   i = p-1
#   for j = p to r-1
#     do if A[j] <= x
#       then i = i+1
#         exchange A[i] and A[j] 
#   exchange A[i+1] and A[r]
#   return i+1


# Quicksort(A, p, r)
#   if p < r
#     then q = Partition(A, p, r)
#       run Quicksort(A, p, q-1)
#       run Quicksort(A, q+1, r)

from bubblesort import bubbleSort
from mergesort import mergeSort
from quicksort import quickSort
from selectionsort import selectionSort