def binary_search_for_pages(target_page, left_page, right_page, num_of_execution):
    
    if left_page+1 >= right_page:
        return -99999
    
    half_page = int((left_page + right_page)/2)

    if half_page == target_page:
        return num_of_execution + 1
    elif half_page > target_page:
        return binary_search_for_pages(target_page, left_page, half_page, num_of_execution+1)
    else:
        return binary_search_for_pages(target_page, half_page, right_page, num_of_execution+1)

test_num = int(input())

for i in range(1, test_num+1):
    nums = list(map(int, input().split(' ')))
    whole_pages = nums[0]
    Pa = nums[1]
    Pb = nums[2]

    num_Pa = binary_search_for_pages(Pa, 1, whole_pages, 0)
    num_Pb = binary_search_for_pages(Pb, 1, whole_pages, 0)

    if num_Pa == num_Pb:
        print(f'#{i} 0')
    elif num_Pa < num_Pb:
        print(f'#{i} A')
    else:
        print(f'#{i} B')