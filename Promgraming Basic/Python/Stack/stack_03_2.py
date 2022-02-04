def path_dfs():
    V, E = map(int, input().split(' '))

    v_list = [0]
    for _ in range(V):
        v_list.append(True)
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
            if not v_list[where_to_go]:
                continue

            v_list[traveler] = False
            traveled_list.append(traveler)
            traveler = where_to_go
            if traveler == G:
                return 1

            break
        else:
            if traveler == S:
                return 0

            v_list[traveler] = False
            traveler = traveled_list.pop(-1)
    

test_of_num = int(input())

for i in range(1, test_of_num+1):

    print(f'#{i} {path_dfs()}')


    

