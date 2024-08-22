import numpy as np

ndarr1 = np.array([1, 5, 1, 4, 4])
ndarr2 = np.array([9, 4, 0, 4, 0])
result = np.lexsort((ndarr2, ndarr1))
# ndarr2 배열을 기준으로 오름차순으로 정렬
# 0, 0, 4, 4, 9
# 동일한 값의 경우 ndarr2 배열의 기준으로 ndarr1 오름차순 한 인덱스를 반환
#
print(result)

surnames = ('Hertz',    'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav') # 1 2 0
ind = np.lexsort((first_names, surnames))
print(ind)


a = [1, 5, 1, 4, 3, 4, 4]  # First sequence
b = [9, 4, 0, 4, 0, 2, 1]  # Second sequence
ind = np.lexsort((b, a))  # Sort by `a`, then by `b`
print(ind)


x = [[1, 2, 3, 4],
     [4, 3, 2, 1],
     [2, 1, 4, 3]]
y = [[2, 2, 1, 1],
     [1, 2, 1, 2],
     [1, 1, 2, 1]]
print(np.lexsort((x, y), axis=1))