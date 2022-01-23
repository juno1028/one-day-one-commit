# 분해합 : 브루트 포스

input_n = int(input())

# 입력된 숫자까지 다 확인해본다.
for num in range(0, input_n+1):
    # 문자열로 만들 경우, 반복이 가능하므로, 문자열로 만든다.
    added_num = 0
    added_num += num
    # 숫자 한 자리씩 더하기
    str_num = str(num)
    # 모든 자리수에 있는 숫자들을 하나씩 더하고,
    for str_num_elem in str_num:
        added_num += int(str_num_elem)
    # 만약, 그 숫자들의 더해진 합이 input_n과 같다면, 그 숫자를 출력하면서 break한다.
    if added_num == input_n:
        print(num)
        break
    elif input_n == num:
        print(0)
