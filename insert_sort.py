import timeit
import random
def insertion_sort(lst):
  for i in range(1, len(lst)):
    key = lst[i]
    j = i-1
    while j >=0 and key<lst[j]:
      lst[j+1] = lst[j]
      j-=1
    lst[j+1] = key
  return lst

arr1 = [random.randint(0, 100) for _ in range(50)]

time_taken = timeit.timeit(lambda: insertion_sort(arr1), number=100)
print("Input array:", arr1)
print("Time taken:", time_taken, "seconds")
print(insertion_sort(arr1))