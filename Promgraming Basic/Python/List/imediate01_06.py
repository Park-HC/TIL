num_test = int(input())
result = []

for i in range(num_test):
    num_list = int(input())
    case_list = list(map(int, input().split()))

    max= case_list[0]
    min= case_list[0]
    for j in range(1, num_list):
        if max < case_list[j]:
            max = case_list[j]
    for j in range(1, num_list):
        if min > case_list[j]:
            min = case_list[j]
    result.append(max - min)

for i in range(num_test):
    print("#{0} {1}".format(i+1, result[i]))



