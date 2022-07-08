num_test = int(input())
result = []

for i in range(num_test):
    num_card = int(input())
    card_input = input()
    card_list = [int(j) for j in card_input]
    numbering = [0] * 10

    for j in card_list:
        for k in range(10):
            if j == k:
                numbering[k] += 1

    max = 0
    count = numbering[0]

    for j in range(1,10):
        if count <= numbering[j]:
            count = numbering[j]
            max = j

    result.append((max, count))

for i in enumerate(result):
    print("#{0} {1} {2}".format(i[0], i[1][0], i[1][1]))
