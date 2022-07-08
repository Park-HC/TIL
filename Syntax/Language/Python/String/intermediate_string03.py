num_of_test = int(input())

for i in range(1, num_of_test + 1):
    short_str = input()
    long_str = input()

    short_str = ''.join(set(short_str))
    count = 0

    for char_short in short_str:
        count_local = 0
        for char_long in long_str:
            if char_short == char_long:
                count_local += 1
        if count_local > count:
            count = count_local

    print(f'#{i} {count}')