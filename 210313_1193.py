import sys

input_num = int(sys.stdin.readline())

n = 1
# 해당 layer에 도달할 때까지 등차수열의 합을 계산한다.
while(True):
    turning_point = (n**2)/2 + n/2
    if turning_point >= input_num:
        number_layer = n
        break
    else:
        n += 1

# layer내에서의 position
position = turning_point - input_num + 1
# 짝수층
if number_layer % 2 == 0:
    num = number_layer - position + 1
    den = position
# 홀수층
else:
    num = position
    den = number_layer - position + 1

num = int(num)
den = int(den)

print(f'{num}/{den}')
