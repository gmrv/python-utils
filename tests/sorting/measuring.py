import timeit

numbers = 100000

code = '''
from sorting.quicksort import quicksort
quicksort([2, 22, 9, 1, 43, 15, 82, 14, 19])
'''
print(timeit.timeit(code, number=numbers), ' - quicksort')

code2 = '''
from sorting.quicksortga import quicksortga
quicksortga([2, 22, 9, 1, 43, 15, 82, 14, 19])
'''
print(timeit.timeit(code2, number=numbers), ' - quicksortga')

code3 = '''
a = [2, 22, 9, 1, 43, 15, 82, 14, 19]
a.sort()
'''
print(timeit.timeit(code3, number=numbers), ' - [].sort()')

# 2.0847202530130744  - quicksort
# 3.052414039033465  - quicksortga
# 0.03247865196317434  - [].sort()