# 해당 데이터의 위치를 하나씩 찾아내는 정렬 O(n2)
array = [8,4,6,2,9,1,3,7,5]

def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		for j in range(i, 0, - 1):
			if array[j - 1] > array[j]:
				array[j - 1], array[j] = array[j], array[j - 1]
		print(array)

print("before: ",array)
insertion_sort(array)
print("after:", array)