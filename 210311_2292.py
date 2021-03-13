# 3 * n^2 + 3 * n + 1 각 층별 최대값

input_num = int(input())
n = 0


def get_max_num_at_same_layer(number):
    return 3*(number**2) + 3*number + 1


max_num = 1
layer_num = 0
while(max_num < input_num):
    layer_num += 1
    max_num = get_max_num_at_same_layer(layer_num)

# 시작을 1층이 아닌 0층으로 했기 때문
print(layer_num + 1)
