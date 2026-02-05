---
title: "열차 관제사 유진의 승강장 배정"
level: "1"
time_limit: 1000
memory_limit: 131072
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Binary Search"]
---

## description
고속열차 관제사 '유진'이는 1번 승강장의 열차 진입 스케줄을 관리합니다. 모든 열차는 $[s, e)$ 형태의 시간 동안 승강장을 점유합니다. ($s$시 정각 진입, $e$시 정각 직전 출발)

새로운 열차가 진입을 요청할 때, 기존에 확정된 열차 스케줄과 **단 1초라도 겹친다면** 안전을 위해 진입을 거절(`DENY`)해야 합니다. 겹치지 않는다면 진입을 승인(`ALLOW`)하고 스케줄에 추가합니다.

정렬 상태를 유지하며 이웃한 예약만 확인하는 $O(N \log N)$ 알고리즘을 구현하세요.



## input_description
- 첫 번째 줄에 열차 진입 요청 횟수 $N$가 주어집니다. 
- $1 \le N \le 100,000$
- 이후 $Q$개의 줄에 걸쳐 각 열차의 진입 시각 $s$와 출발 시각 $e$가 공백으로 구분되어 주어집니다. 
- $0 \le s < e \le 10^9$

## output_description
- 각 요청에 대해 승인되면 `ALLOW`, 거절되면 `DENY`를 한 줄에 하나씩 출력합니다.
- 입력이 들어오는 즉시 결과를 출력해야 합니다.

# samples

### input 1
```
3
10 20
15 25
20 30
```

### output 1
```
ALLOW
DENY
ALLOW
```


### input 2
```
3
50 100
0 30
20 60
```

### output 2
```
ALLOW
ALLOW
DENY
```


### input 3
```
4
10 50
60 100
110 150
55 58
```

### output 3
```
ALLOW
ALLOW
ALLOW
ALLOW
```

