# Instruction

## Instruction Set

- 컴퓨터에서 지원하는 명령어들의 집합
- 다른 컴퓨터들은 다른 인스트럭션 셋을 가지고 있음
  - 하지만 꽤 많은 부분이 닮아있음
- 초창기 컴퓨터는 아주 간단한 인스트럭션 셋을 가지고 있음
- 이후 CISC(Complex Instruction Set Computer)라는 방식이 나옴
  - Intel 프로세서 등이 이 방식을 체택함
- 현대 컴퓨터는 다시 간단한 인스트럭션 셋을 지향함
  - MIPS
  - Reduced Instruction Set Computer(RISC)

### ISA(Instruction Set Architecture)

- 하드웨어와 Lowest Level Software(OS) 사이의 추상적인 인터페이스
- instruction, 레지스터, 메모리 접근, I/O 등 어떤 명령을 통해서든 모든 정보를 인스트럭션을 통해 컴퓨터에 전달됨

### ABI(Application Binary Interface)

- 시스템 소프트웨어 인터페이스와 ISA의 조합
- 컴퓨터에 binary portability하는 기준
- 어떤 컴퓨터에서 실행되는 프로그램은 ABI가 같은 다른 컴퓨터에서도 실행이 보장됨

### MIPS

- 현대 ISA의 기본

- 예전 임베디드 코어 마켓에서 활용됨
  - 현재는 ARM으로 옮겨짐
- 본 강의의 기본



## Arithmetic Operations

- 구조상 3개의 operands가 필요함
  - `a gets b + c`
  - `a <- b + c`
- 1. Simplicity Favours Regularity 원칙을 따름



```C
// C 코드
f = (g + h) - (i + j);

// Compiled MIPS code
add t0, g, h  # temp t0 = g + h
add t1, i, j  # temp t1 = i + j
sub f, t0, t1 # temp f = t0 - t1
```



## Register Operands

- Arithmetic Instructions는 Register Operands의 연산
- MIPS에서는 32 * 32 bit 레지스터 파일을 사용
  - 자주 사용하는(접근하는) 데이터를 저장하기 위해 사용됨
  - 0 ~ 31까지 번호가 있음
  - 32 비트 데이터는 word라고 불림(4 bytes)
- Assembler names
  - $t0, $t1, ..., $t9 는 휘발성 값에 붙여짐
  - $s0, $s1, ..., $s0 는 저장된 변수에 붙여짐
- 레지스터는 아주 빠르기 때문에 가능한 레지스터를 많이 이용해야 성능 향상에 도움이 됨!

```C
// C code
f = (g + f) - (i + j);
// f, ..., j in $s0, ..., $s4

// Comiled MIPS code
add $t0, $s1, $s2
add $t1, $s3, $s4
sub $s0, $t0, $t1
```



## Byte Addresses

- 대부분의 프로세서(아키텍쳐)들은 byte(8 bit)가 기본 단위
- MIPS는 32 bits(MIPS-32)
  - 어떤 데이터 명령어를 word 단위로 계산(할양)

### Big Endian / Little Endian

- 데이터를 메모리에 저장하는 대표적인 방법들
- Big Endian
  - 어느 데이터를 이루는 값 중 자리 수가 높은 것을 끝에 저장함
- Little Endian
  - 어느 데이터를 이루는 값 중 자리 수가 낮은 것을 끝에 저장함



## Memory Operands

- 메인 메모리는 (composite) 데이터를 저장
  - 배열, 구조체, 다이나믹 데이터 등
- Arithmetic Operation
  - 메모리에 있는 값은 레지스터에 올림
  - 연산 후 결과를 레지스터에서 메모리에 저장함
  - => Load/Store Architecture
    - 메모리에 접근하는 Load 명령어와 레지스터에 접근하는 Store 명령어가 각각 지정되어 있음
    - MIPS, RISC 등에서 지원
    - 인텔의 CISC 등에서는 지원하지 않음
- 메모리의 기본 단위는 바이트
- 메모리는 word-aligned 되어 있음
  - 메모리의 주소는 4 bytes로 할당 되어 있음
- MIPS는 Big Endian

```c
// C code
g = h + A[8]
    // g in $s1, h in $s2, base address of A in $s3
    
// Compiled MIPS code
    // Index 8 requires offset of 32
    // because, 4bytes per word!
lw $t0, 32($s3)		// lw: load word  // $t0 = $s3 + 32
add $s1, $s2, $t0
```

```c
// C code
A[12] = h + A[8];
	// h in $s2, base address of A in $s3

// Compiled MIPS code
	// Index 8 requires offset of 32, 12 requires 48!
lw $t0, 32($s3)		// load word
add $t0, $s2, $t0
sw $t0, 48($s3)		// store word
```



## Registers vs Memory

- 레지스터는 메모리보다 훨씬 빠름
- 메모리 데이터를 다룰 때는 load와 store 명령어를 통해 레지스터에 올려야 됨
  - instructions을 더 써야 함
- 가능한 register를 최대한 활용해야 함
  - 자주 사용하지 않는 변수는 메모리에 올림
  - 레지스터를 최적화하는 것이 중요
- 레지스터는 보통 어드레스보다 짧으므로 code density가 높아짐!



## MIPS Register File

- 32개의 32 bit 레지스터를 가짐
- 2개의 read port
- 1개의 write port
- 에셈블러 용, return 값용, argument 용, 임시 값용, 저장 변수용, 스택 포인터 등등 레지스터 마다 사용처가 정해져 있음



## Immediate Operands

- 오퍼렌드 중 하나가 상수인 오퍼렌드

```
addi $s3, $s3, 4
```

- subtract은 이를 지원하지 않음

```
addi $s2, $s1, -1
```

### Constant Zero

- MIPS에서는 레지스터 0($zero)가 0의 값을 가짐
- 절대 덧씌워지지 않는 레지스터
- 생각보다 자주 사용되는 연산자
  - 이동, 복사에서도 레지스터 0을 사용

```
// move between registers
add $t2, $s1, $zero
```



## 프로세스의 4가지 디자인 원칙

### 1. Simplicity Favours Regularity

- 정규성은 실행을 간단하게 만든다
- 간단하게 만들면 저 비용으로 고성능을 만들기 쉽다

### 2. Smaller is Faster

- 작은 것이 더 빠르다

### 3. Make the Common Case Fast

- 작은 상수는 자주 사용한다
- 이 상수들은 load instruction 보다 immediate operand를 사용하면 성능을 향상할 수 있을 것이다!

