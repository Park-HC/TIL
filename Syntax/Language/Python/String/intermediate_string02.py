def search_para_row(N, M, words):
    for i in range(N):
        word = words[i]

        for j in range(0, N-M+1):
            check = True

            for k in range(M):
                if word[j + k] != word[j + M - k - 1]:
                    check = False
                    break
            if check:
                return word[j : j + M]
    
    return None


def search_para_col(N, M, words):
    for i in range(N):
        word = ''
        
        for j in range(N):
            word = word + words[j][i]
        
        for j in range(0, N-M+1):
            check = True

            for k in range(M):
                if word[j + k] != word[j + M - k - 1]:
                    check = False
                    break

            if check:
                return word[j : j + M]
    
    return None

num_of_test = int(input())

for i in range(1, num_of_test + 1):
    numbs = list(map(int, input().split(' ')))
    N = numbs[0]
    M = numbs[1]

    words = list()

    for _ in range(N):
        words.append(input())

    para = search_para_row(N, M, words)

    if para == None:
        para = search_para_col(N, M, words)

    print(f'#{i} {para}')