# 맛집의 줄 서기 알바

## 문제 설명
주인공 **민수**는 요즘 SNS에서 가장 핫한 '데브 버거(Dev Burger)'에서 대기 줄 관리 아르바이트를 시작했습니다. 
이 가게는 **먼저 온 손님이 먼저 들어가는(FIFO)** 원칙을 철저히 지킵니다.

민수는 큐(Queue) 자료구조의 원리를 이용하여 다음 5가지 기능을 수행하는 프로그램을 작성해야 합니다.

1.  **enqueue X**: 손님 이름 `X`가 줄의 맨 뒤에 합류합니다. (Enqueue)
2.  **dequeue**: 가장 앞에 있는 손님이 식당으로 입장합니다. 입장한 손님의 이름을 출력하고 줄에서 제거합니다. 만약 줄이 비어있다면 `-1`을 출력합니다. (Dequeue)
3.  **size**: 현재 줄을 서서 기다리고 있는 손님이 총 몇 명인지 출력합니다.
4.  **empty**: 줄이 비어있으면 `1`, 비어있지 않으면 `0`을 출력합니다.
5.  **front**: 현재 줄의 가장 앞에 있는 손님의 이름을 확인만 합니다. 만약 줄이 비어있다면 `-1`을 출력합니다.

---

## 입력 형식 (Input Format)
* 첫 번째 줄에 처리해야 할 명령의 수 $N$이 주어집니다. ($1 \le N \le 10,000$)
* 두 번째 줄부터 $N$개의 줄에 걸쳐 명령이 하나씩 주어집니다.
* 이름 $X$는 영문 소문자이며, 길이는 10자를 넘지 않습니다.

## 출력 형식 (Output Format)
* 출력 명령(`dequeue`, `size`, `empty`, `front`)이 주어질 때마다 결과를 한 줄씩 출력합니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
```
8
enqueue minsu
enqueue chulsu
front
dequeue
size
empty
dequeue
dequeue
```

**Output:**
```
minsu
minsu
1
0
chulsu
-1
```

### 예시 2
**Input:**
```
7
enqueue alice
empty
dequeue
enqueue bob
size
dequeue
empty
```

**Output:**
```
0
alice
1
bob
1
```

* **enqueue alice**: `alice`가 줄을 섭니다. $\rightarrow$ `[alice]`
* **empty**: 줄이 안 비었으므로 `0`을 출력합니다.
* **dequeue**: `alice`가 입장합니다. $\rightarrow$ `alice` 출력 (남은 줄: `[]`)
* **enqueue bob**: `bob`이 줄을 섭니다. $\rightarrow$ `[bob]`
* **size**: 1명이 줄 서 있으므로 `1`을 출력합니다.
* **dequeue**: `bob`이 입장합니다. $\rightarrow$ `bob` 출력 (남은 줄: `[]`)
* **empty**: 줄이 비었으므로 `1`을 출력합니다.
