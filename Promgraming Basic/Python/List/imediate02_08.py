def bubble_swap(complex_list):

    k = len(complex_list)-1
    for i in range(5):
        for j in range(k):
            if complex_list[j] > complex_list[j+1]:
                complex_list[j], complex_list[j+1] = complex_list[j+1], complex_list[j]
        k -= 1
    
    for i in range(5):
        for j in range(len(complex_list)-6, i, -1):
            if complex_list[j-1] > complex_list[j]:
                complex_list[j-1], complex_list[j] = complex_list[j], complex_list[j-1]

def twist_list(sorted_list):
    result = []

    for i in range(5):
        result.append(sorted_list[-i-1])
        result.append(sorted_list[i])
    
    return result

test_num = int(input())

for i in range(1, test_num+1):
    list_num = int(input())

    nums = list(map(int, input().split()))

    bubble_swap(nums)
    news = twist_list(nums)

    print(f'#{i}', ' '.join(map(str,news)))