---
title: "미미의 369 게임"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
친구들과 369 게임을 하던 '미미'는 숫자가 커질수록 박수를 쳐야 할지 말지 헷갈리기 시작했습니다.<br/>
369 게임의 규칙은 다음과 같습니다.
1. 1부터 입력받은 숫자 N까지 차례대로 말합니다.
2. 숫자에 3, 6, 9가 하나라도 포함되어 있다면 숫자 대신 clap을 출력합니다.
3. 그 외의 경우에는 숫자를 그대로 출력합니다.
'미미'를 도와 1부터 N까지 규칙에 맞게 결과를 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 마지막 숫자 N이 주어집니다. ($1 \le N \le 100$)

## output_description
- 1부터 N까지의 결과를 공백으로 구분하여 한 줄에 출력합니다.

# samples

### input 1
```
10
```

### output 1
```
1 2 clap 4 5 clap 7 8 clap 10
```


### input 2
```
16
```

### output 2
```
1 2 clap 4 5 clap 7 8 clap 10 11 12 clap 14 15 clap
```
