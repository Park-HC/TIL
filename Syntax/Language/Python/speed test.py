import time

N = 10000
a = [i for i in range(N)]

print("top은 뒤에서부터, head는 앞에서부터 제거!")


b = a[:]
start = time.time()
while b:
    b.pop()
print("pop top speed: ", time.time() - start)

b = a[:]
start = time.time()
while b:
    b.pop(0)
print("pop head speed: ", time.time() - start)


b = a[:]
start = time.time()
for i in range(N - 1, -1, -1):
    b.remove(i)
print("remove top speed: ", time.time() - start)

b = a[:]
start = time.time()
for i in range(N):
    b.remove(i)
print("remove head speed: ", time.time() - start)


b = a[:]
start = time.time()
while b:
    del b[-1]
print("del top speed: ", time.time() - start)

b = a[:]
start = time.time()
while b:
    del b[0]
print("del head speed: ", time.time() - start)


b = a[:]
start = time.time()
while b:
    b = b[:-1]
print("slice top speed: ", time.time() - start)

b = a[:]
start = time.time()
while b:
    b = b[1:]
print("slice head speed: ", time.time() - start)
