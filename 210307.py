# 시간초과 나온 코드 - 스택/큐를 활용하지 않았다.


# def solution(prices):
#     answer = [0] * len(prices)

#     index = 0
#     for criteria_price in prices:
#         temp = 0
#         for comparing_price in prices[index+1:]:
#             answer[index] = temp + 1
#             if criteria_price <= comparing_price:
#                 temp += 1
#             else:
#                 break
#         index += 1

#     return answer


# result = [4, 3, 1, 1, 0]

# 스택/큐를 활용한 코드

def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    st = []
    for i in range(n):
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        st.append(i)
        print(st)
    while st:
        top = st.pop()
        answer[top] = n - top - 1

    # print(answer)

    return answer


solution([1, 2, 3, 2, 3])
