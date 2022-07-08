# Python

## SWEA

### list를 print하는 방법

```python
print(f'#{test}', end='')
for num in numbers:
    print(f' {num}', end='')
print()
```



```python
str_numbers = [str(num) for num in numbers]
result = ' '.join(str_numbers)
print(f'#{test} {result}')
```



```python
print(f'#{test}')
print(*numbers, sep=' ')
```

