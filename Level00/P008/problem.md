---
title: "루나의 드론 점검"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
탐험가 루나는 탐험용 드론을 점검하고 있습니다.
드론들은 상태 코드로 관리되며,

- 1 : 정상 작동
- 0 : 고장

을 의미합니다.

드론 상태 정보가 주어질 때, 정상적으로 작동 중인 드론의 개수를 구하는 프로그램을 작성하세요.



## input_description
- 첫째 줄에 드론의 개수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수(0 또는 1)가 공백으로 구분되어 주어집니다.

## output_description
- 정상 작동 중인 드론의 개수를 출력합니다.

# samples

### input 1
```
6
1 0 1 1 0 1
```

### output 1
```
4
```

### input 2
```
4
0 0 0 0
```

### output 2
```
0
```
