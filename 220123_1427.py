# 소트인사이드 : 정렬
# 특별한 알고리즘 없이, 정렬만 하면 되는듯?


def sort_inside(number: int):
    listed_number = list(str(number))
    # 정렬시킨다. 처음에 sorted 함수 안에 넣는게 아니라, sort로 했더니 None 뜸
    sorted_list = sorted(listed_number, reverse=True)
    # 문자열로 join 해준다.
    joined_sorted_list = "".join(sorted_list)
    return joined_sorted_list


input_n = int(input())
print(sort_inside(input_n))
