def solution(array, commands):
    def get_sliced_array(arr, command):
        start_point = command[0]
        end_point = command[1]
        sliced_arr = arr[start_point-1:end_point]

        return sliced_arr

    def sort_and_select_number(arr, command):
        sorted_arr = sorted(arr)
        selected_number_index = command[2]

        selected_number = sorted_arr[selected_number_index-1]

        return selected_number

    result_arr = []
    for command in commands:
        sliced_array = get_sliced_array(array, command)
        selected_number = sort_and_select_number(sliced_array, command)
        result_arr.append(selected_number)

    return result_arr


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
