import sys
# 1. 단위의 갯수와 총 금액을 입력 받는다.
unit_count, total = map(int, sys.stdin.readline().split())

# 2. 단위 리스트에 단위들을 저장한다.
unit_list = []
for _ in range(unit_count):
    unit = int(input())
    unit_list.insert(0, unit)

# 3. 가장 큰 단위부터 한 개씩 빼나간다.
count = 0
for unit in unit_list:
    if unit <= total:
        how_many_unit = total // unit
        count += how_many_unit
        total = total % unit
        how_many_unit = 0
    if total == 0:
        break

print(count)
