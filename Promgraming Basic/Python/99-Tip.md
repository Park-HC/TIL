  # Tip

  - 오류 해결 때 메세지, 특히 'unpack'이 있는 부분을 유심히 살펴보자

    ```python
    float('INF')
    # python에서 표현할 수 있는 가장 큰 수
    ```

    

## 코딩

- for 반복문을 쓸 때, 반복자가 아래 쓰이지 않는다면 _로 대체할 수 있음

```python
n = 5
m = 9

star = '*'

for _ in range(m):
    for _ in range(n):
        print(star, end = '')
    else:
        print()
```



- dir을 통해 객체에 포함된 인자와 함수들을 확인할 수 있음

  ```python
  dir(list)
  """
  ['__add__',
   '__class__',
   '__class_getitem__',
   '__contains__',
   '__delattr__',
   '__delitem__',
   '__dir__',
   '__doc__',
   '__eq__',
   '__format__',
   '__ge__',
   '__getattribute__',
   '__getitem__',
   '__gt__',
   '__hash__',
   '__iadd__',
   '__imul__',
   '__init__',
   '__init_subclass__',
   '__iter__',
   '__le__',
   '__len__',
   '__lt__',
   '__mul__',
   '__ne__',
   '__new__',
   '__reduce__',
   '__reduce_ex__',
   '__repr__',
   '__reversed__',
   '__rmul__',
   '__setattr__',
   '__setitem__',
   '__sizeof__',
   '__str__',
   '__subclasshook__',
   'append',
   'clear',
   'copy',
   'count',
   'extend',
   'index',
   'insert',
   'pop',
   'remove',
   'reverse',
   'sort']
  """
  ```

  - **코테 등에 사용하면 편함!**
