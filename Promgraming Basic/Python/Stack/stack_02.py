def check_bracket(words):
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']

    stack_bracket = []

    for word in words:
        if word in left_brackets:
            stack_bracket.append(word)
        elif word in right_brackets:
            if stack_bracket == [] or left_brackets[right_brackets.index(word)] != stack_bracket.pop(-1):
                return 0
    
    if stack_bracket:
        return 0
    else:
        return 1

test_of_num = int(input())

for i in range(1, test_of_num+1):
    code = input()

    print(f'#{i} {check_bracket(code)}')
        



