def mk_pattern(small_str):

    pattern = small_str

    for i in range(5, 0, -1):
        if len(small_str) < i:
            continue

        pattern = small_str[-i: ]
        k = True

        for j in range(len(pattern) - 1):
            if pattern[j] in pattern[j+1:]:
                break
        else:
            break
    
    return pattern


def boyer_moore(small_str, long_str):

    bool_check = 0

    pattern = mk_pattern(small_str)
    pattern_length = len(pattern)
    check_idx = pattern_length -1

    print(f'pattern: {pattern}, length: {pattern_length}')

    i = 1

    while check_idx < len(long_str):

        print(f'{i}th trial')

        if long_str[check_idx] in pattern:
            
            print(f'We find it! {long_str[check_idx]} in {pattern}!')
            
            k = pattern.find(long_str[check_idx])
            check_idx += (pattern_length - (k+1))

            print(f'Now, {long_str[check_idx]} is last of {pattern}!')

            if check_idx < len(small_str):
                check_idx += pattern_length
            else:
                if small_str == long_str[(check_idx+1 - len(small_str)):check_idx+1]:
                    bool_check = 1
                    break
                else:
                    check_idx += pattern_length
        
        else:

            print(f'No {long_str[check_idx]} not in {pattern}!')

            check_idx += pattern_length
        
        i += 1


    return bool_check

num_of_test = int(input())

for i in range(1, num_of_test + 1):
    sm_str = input()
    lg_str = input()

    print(f'#{i} {boyer_moore(sm_str, lg_str)}')