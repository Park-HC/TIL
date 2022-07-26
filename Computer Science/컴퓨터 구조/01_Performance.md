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



## CPU Clocking

- Clock Period
  - Rising Edge, Falling Edge 하나씩
  - Clock cycle에 걸리는 시간
- Clock Frequency
  - 1초에 수행되는 Clock cycle의 수
- Clock Period는 Clock Frequency에 반비례
  - `CC = 1/CR`



### CPU Time

- CPU Clock Cycles * Clock Cycle Time
  - CPU Clock Cycles / Clock Rate
- 향상법
  - Clock Cycle 수를 줄이거나
  - Clock Rate를 높인다



### Instruction count and CPI

```
Clock Cycles = Instruction Count * Cycles per Instruction
CPU Time = Instruction Count * CPI * Clock Cycle Time
		= Instruction Count * CPI / Clock Rate
```

- Instruction 수는 프로그램이나 ISA, 컴파일러에 의해 정해짐

### CPI

```
Clock Cycles = (시그마)CPI * Instruction Count

// Weighted Average CPI
CPI = Clock Cycles / Instruction Count
	= (시그마) CPI * Instruction count/(총 Instruction Count)
```



### 총정리

``` 
CPU Time = (Instructions / Program) * (Clock Cycles / Instruction) * (Seconds / Clock Cycle)
		= IC * CPI * Clock Period
```

- 알고리즘은 IC에 영향, CPI에도 연관 가능
- 프로그래밍 언어는 IC와 CPI에 영향
- 컴파일러는 IC와 CPI에 영향
- 인스트럭션 집합 아키텍쳐(ISA)는 IC, CPI, Clock Period 모두에 영향을 미침



## Power Wall

### Power

```
Power = Capacitive load * Voltage ** 2 * Frequency
```

- Power을 유지하면서 Frequency를 높이고 싶다면 Capacitive load나 Voltage를 낮추어야 한다
  -  2005년까지 Voltage는 5V에서 1V로 낮추어 졌으나 그 이하는 힘들었다



### Power Wall

- Voltage를 도저히 낮출 수 없다!
- 이보다 열을 덜 내게 만들 수 없다!



### Multiprocessor Peformance

- Multicore Microprocessors
  - 듀얼 코어, 쿼드 코어...
- Parallel Programming이 용이해짐
  - instruction 레벨에서 parallel하게 처리할 수 있음
  - 하지만 프로그래밍과 디버깅이 어렵고 로드 밸런싱 문제가 발생할 수 있으며
  - 프로세싱 간에 커뮤니케이션과 동기화를 조정하기 어려움



### SPEC CPU Benchmark

- SPEC에서 만든 표준 CPU 성능 측정 기준
- I/O는 거의 무시하고 CPU 성능에 더 비중을 둠 



## Pitfall: Amdahl's Law

```
T_imporved = T_affected / improvement factor + T_unaffected
```

- 하나의 컴포넌트의 성능을 향상시키면 그 컴포넌트가 전체 시스템에서 차지하는 비중에 비례하는 만큼 전체 시스템의 성능이 향상된다.
- Corollary
  - 전체 성능에서 많은 비중을 차지하는 것을 더 빠르게 만들어라!



## Fallacy: Low Power at Idle

- i7 power benchmark
  - At 100% load: 258W
  - At 50% load: 170W(66%)
  - At 10% load: 121W(47%)
- Google data center
  - Mostly operates at 10~50% load
  - At 100% load less than 1% of the time

=> 전원 사용량은 가능한 로드 양에 비례하게 프로세스를 만들자!



## Pitfall: MIPS as a Performance Metric

```
MIPS = Instruction count / (Execution time % 10^6)
	= Instruction count ( Instruction count * CPI * 10^6 / Clock Rate)
	= Clock rate / (CPI * 10^6)
```



- MIPS
  - Millions of Instructions Per Second: 1초에 몇 백만개의 명령어를 실행하는가?
- 단점
  - 컴퓨터 마다 ISA가 다른 것을 반영하지 않음
  - 명령어 마다 CPU Time 소모가 다른 것을 감안하지 않음
  - CPU에 따라 CPI가 달라지