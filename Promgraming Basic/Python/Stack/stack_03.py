def path_dfs():
    V, E = map(int, input().split(' '))

    v_list = list(range(1, V+1))
    e_list = [[]]
    for _ in range(V):
        e_list.append([])
    # V,E로 정점 리스트와 대변 리스트 초기화

    for _ in range(E):
        a, b = map(int, input().split(' '))
        e_list[a].append(b)

    S, G = map(int, input().split(' '))
    traveler = S
    traveled_list = []

    while True:
        for where_to_go in e_list[traveler]:
            if where_to_go in traveled_list or where_to_go not in v_list:
                continue

            traveled_list.append(traveler)
            traveler = where_to_go

            if traveler == G:
                return 1

            break
        else:
            if traveler == S or traveled_list == []:
                return 0
            v_list.remove(traveler)
            traveler = traveled_list.pop(-1)
    

test_of_num = int(input())

for i in range(1, test_of_num+1):

    print(f'#{i} {path_dfs()}')


    

