def find_sub_group(remain_to_objective, start_idx, num_of_rest):

    result = 0

    if remain_to_objective == 0 and num_of_rest == 0:
        return 1

    if num_of_rest < 0 or remain_to_objective < 0 or start_idx >= 13:
        return 0
    
    for i in range(start_idx, 13):
        result += find_sub_group(remain_to_objective - i, i+1, num_of_rest-1)
    
    return result

test_num = int(input())

for i in range(1, test_num+1):
    nums = list(map(int, input().split(' ')))
    num_of_pick = nums[0]
    objective = nums[1]

    print(f'#{i} {find_sub_group(objective, 1, num_of_pick)}')
