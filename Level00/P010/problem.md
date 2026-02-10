---
title: "지우의 성적 판정기"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Loop"]
---

## description
학원 조교 지우는 학생들의 점수를 입력하면 학점을 자동으로 알려주는 프로그램을 만들려고 합니다.
각 학생의 점수에 따라 학점은 아래 규칙으로 결정됩니다.

- 90 이상: A
- 80 이상: B
- 70 이상: C
- 그 외: F

학생 수와 각 학생의 점수가 주어질 때, 각 학생의 학점을 한 줄씩 출력하는 프로그램을 작성하세요.



## input_description
- 첫째 줄에 학생 수 N이 주어집니다. (1 ≤ N ≤ 100)
- 둘째 줄에 N개의 정수 점수가 공백으로 구분되어 주어집니다. (0 ≤ 점수 ≤ 100)

## output_description
- N줄에 걸쳐 각 학생의 학점을 순서대로 출력합니다.

# samples

### input 1
```
5
95 83 70 69 100
```

### output 1
```
A
B
C
F
A
```

### input 2
```
3
0 80 90
```

### output 2
```
F
B
A
```
