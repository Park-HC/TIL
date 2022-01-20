num_test = int(input())
result = []

for i in range(num_test):
    vari = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    sum_list = []

    for j in range(vari[0] - vari[1] + 1):
        sum_list.append(sum(num_list[j:j+vari[1]]))


    result.append(max(sum_list) - min(sum_list))

for i in range(num_test):
    print("#{0} {1}".format(i+1, result[i]))
