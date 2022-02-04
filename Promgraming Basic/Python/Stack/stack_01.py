"""
    20 X (10 * N) 도형의 경우의 수를 Q(N)이라 하면
    Q(N) = Q(N-1) + 3 * Q(N-2) - Q(N-2)이다.
    한 단계 전 도형에서 10 직사각형 하나를 추가한 경우에
    두 단계 전 도형에서 20 정사각형을 채우는 3가지 방법을 더하고
    위 두 단계에서 겹치게 되는, 20 정사각형을 세로로 긴 사각형 2개로 채우는 방법을 뺀 횟수이다.
    세로로 긴 사각형 2개로 채운다면, 결국 두 사각형 중 왼쪽 사각형은 N-2 와 합쳐져 N-1의 경우가 되기 때문이다.
""" 

def sqaure_case(num):
    global memo

    if num >= 2 and len(memo) <= num:
        memo.append(sqaure_case(num-1) + 2*sqaure_case(num-2))
    return memo[num]

memo = [1, 3]

test_of_num = int(input())

for i in range(1, test_of_num+1):
    N = int(input()) // 10

    print(f'#{i} {sqaure_case(N-1)}')