from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

rotating_list = list(range(1, n+1))

dq = deque()
# 초기 index 값
index_num = k-1
while(True):
    dq.append(rotating_list.pop(index_num))
    if len(rotating_list) == 0:
        break
    index_num = index_num + k - 1
    index_num = index_num % len(rotating_list)

formatted_str_dq = str(list(dq))
print(f'<{formatted_str_dq[1:len(formatted_str_dq)-1]}>')
