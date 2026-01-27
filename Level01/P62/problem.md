# 우체국장 베리의 줄 세우기

## 문제 설명
우체국장 '베리'는 두 개의 창구($A$와 $B$) 앞에 늘어선 대기열이 불공평하게 길어지는 것을 매우 싫어합니다. 베리는 두 줄의 인원수 차이가 $1$보다 커지면, 더 긴 줄의 **맨 앞사람**을 다른 줄의 **맨 뒷자리**로 옮겨 균형을 맞춥니다.

베리의 줄 세우기 규칙은 다음과 같습니다:
1. 두 줄의 인원수를 각각 $L_A$와 $L_B$라고 할 때, $|L_A - L_B| \le 1$이 될 때까지 다음 과정을 반복합니다.
2. 만약 $L_A > L_B + 1$ 이라면, $A$ 줄의 가장 앞에 있는 사람을 꺼내 $B$ 줄의 가장 뒤에 세웁니다.
3. 만약 $L_B > L_A + 1$ 이라면, $B$ 줄의 가장 앞에 있는 사람을 꺼내 $A$ 줄의 가장 뒤에 세웁니다.
4. 모든 이동은 한 번에 한 명씩 차례대로 일어납니다.

처음 두 창구의 대기열 상태가 주어질 때, 베리의 관리가 끝난 후 두 줄의 최종 상태를 구하는 프로그램을 작성하세요.

---
## 입력 형식 (Input Format)
- 첫 번째 줄에 $A$ 줄의 인원수 $N_A$와 $B$ 줄의 인원수 $N_B$가 공백으로 구분되어 주어집니다. ($0 \le N_A, N_B \le 500$)
- 두 번째 줄에 $A$ 줄에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다. ($N_A=0$이면 빈 줄입니다.)
- 세 번째 줄에 $B$ 줄에 서 있는 사람들의 이름이 공백으로 구분되어 주어집니다. ($N_B=0$이면 빈 줄입니다.)

## 출력 형식 (Output Format)
- 첫 번째 줄에 최종 $A$ 줄의 상태를 이름 사이 공백을 두어 출력합니다.
- 두 번째 줄에 최종 $B$ 줄의 상태를 이름 사이 공백을 두어 출력합니다.
- 줄이 비어있다면 `Empty`를 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
```
5 1
Alice Bob Charlie Dave Eve
Frank
```

**Output:**
```
Charlie Dave Eve
Frank Alice Bob
```

- 초기 상태
  - $A = [\text{Alice, Bob, Charlie, Dave, Eve}]$
  - $B = [\text{Frank}]$ 
  - ($5:1$ 차이 $4$)
- 1차 이동
  - $A$ 앞의 Alice를 $B$ 뒤로. 
  - $A = [\text{Bob, Charlie, Dave, Eve}]$
  - $B = [\text{Frank, Alice}]$ 
  - ($4:2$ 차이 $2$)
- 2차 이동
  - $A$ 앞의 Bob을 $B$ 뒤로. 
  - $A = [\text{Charlie, Dave, Eve}]$
  - $B = [\text{Frank, Alice, Bob}]$ 
  - ($3:3$ 차이 $0$)
- 차이가 $1$ 이하이므로 종료.

### 예시 2
**Input:**
```
1 4
Tom
Jerry Mickey Donald Goofy
```

**Output:**
```
Tom Jerry
Mickey Donald Goofy
```

- 초기 상태 
  - $1:4$ (차이 $3$)
- $B$ 앞의 Jerry를 $A$ 뒤로 이동
  - $A = [\text{Tom, Jerry}]$
  - $B = [\text{Mickey, Donald, Goofy}]$ 
  - ($2:3$ 차이 $1$)
- 차이가 $1$ 이하이므로 종료.

### 예시 3
**Input:**
```
2 2
Pikachu Raichu
Charmander Squirtle
```

**Output:**
```
Pikachu Raichu
Charmander Squirtle
```
