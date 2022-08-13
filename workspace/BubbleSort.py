# 인접한 두 수를 비교하며 정렬 O(n2) 시간복잡도
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print("before: ",array)
bubble_sort(array)
print("after:", array)