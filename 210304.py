# 프로그래머스 : 완주하지 못한 선수(해쉬)


def solution(participants, completions):
    completion_dict = {}
    for completion in completions:
        if completion in completion_dict:
            completion_dict[completion] += 1
        else:
            completion_dict[completion] = 1

    for participant in participants:
        if (participant not in completion_dict) or (completion_dict[participant] == 0):
            return participant
        completion_dict[participant] -= 1
