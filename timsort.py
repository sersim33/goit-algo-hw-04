import timeit
import random

arr2 = [random.randint(0, 100) for _ in range(100)]
arr2.sort()  


time_taken = timeit.timeit(lambda: arr2.sort(), number=100)

print("Time taken for arr2.sort():", time_taken*1000, "seconds*1000")
print(arr2)