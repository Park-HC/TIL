# Performance

## 기준

### Response Time

- latency

- 하나의 일을 수행하는 데 걸리는 시간
- 적을 수록 성능이 좋음

### Throughput

- 단위 시간단 몇개의 일을 하는가
- 높을 수록 성능이 좋음

### Response Time vs Throughput

- 만약 프로세서를 더 빠른 것을 바꾸었다면
  - Response Time이 줄어듦
  - Throughput이 증가함
- 만약 프로세서를 더 추가했다면
  - Response Time은 동일함
  - Throughput은 증가함
- 이 문서는 Response Time을 위주로 작성됨



## Relative Perormance

```
Performance = 1/Execution Time

Performance_x / Performance_y = Execution_Time_y / Execution_Time_x = n
컴퓨터 x는 컴퓨터 y보다 n배 빠르다!
```



## Measuring Execution Time

### Elapsed time

- Total response time, including all aspects
  - 프로세싱, I/O, OS 오버헤드, idle time
- System Performance



### CPU time

- 주어진 일을 프로세싱 하는데 걸리는 시간
  - I/O 등 기타 작업 시간 제외
- user CPU time과 system CPU time으로 나뉨



### CPU Clocking

- Clock Period
  - Rising Edge, Falling Edge 하나씩
  - Clock cycle에 걸리는 시간
- Clock Frequency
  - 1초에 수행되는 Clock cycle의 수
- Clock Period는 Clock Frequency에 반비례