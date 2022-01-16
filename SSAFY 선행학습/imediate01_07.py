num_test = int(input())
result = []

for i in range(num_test):
    vari = list(map(int, input().split()))
    charging_stop = list(map(int, input().split()))
    charge_num = 0
    position = 0
    possible = True

    while possible:
        if position + vari[0] >= vari[1]:
            break
        possible = False

        for j in range(position + vari[0], position, -1):
            if j in charging_stop:
                position = j
                charge_num += 1
                possible = True
                break
        
        if possible == False:
            charge_num = 0
            break

    result.append(charge_num)

for i in range(num_test):
    print("#{0} {1}".format(i+1, result[i]))
