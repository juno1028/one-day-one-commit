# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

distance_list = [abs(x), abs(w-x), abs(y), abs(h-y)]

print(min(distance_list))
