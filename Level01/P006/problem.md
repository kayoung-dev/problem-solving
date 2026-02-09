---
title: "구름이의 책 찾기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Array"]
---

## description
도서관 사서 **'구름이'** 는 엉망진창으로 섞여 있는 책장 정리를 맡게 되었습니다. 책장에는 $N$권의 책이 무작위로 꽂혀 있습니다.

**'구름이'** 가 찾고자 하는 특정 책의 제목이 주어졌을 때, 그 책이 **왼쪽에서 몇 번째** 위치에 꽂혀 있는지 찾아내는 프로그램을 작성하세요.

* 만약 책이 존재하면 그 위치(1부터 시작)를 출력합니다.
* 만약 찾는 책이 책장에 없다면 `-1`을 출력합니다.


## input_description
- 첫 번째 줄에 책의 총 개수 $N$이 주어집니다. ($1 \le N \le 100$)
- 두 번째 줄에 찾고자 하는 **목표 책 제목**이 주어집니다.
- 세 번째 줄에 책장에 꽂힌 $N$권의 책 제목들이 공백으로 구분되어 주어집니다.
- 책 제목은 영문 대소문자, + 로만 구성됩니다.

## output_description
- 찾는 책의 위치(1부터 시작하는 순서)를 정수로 출력합니다.
- 책이 없다면 `-1`을 출력합니다.

# samples

### input 1
```
5
Python
Java C++ Python Ruby Go
```

### output 1
```
3
```


### input 2
```
3
HTML
CSS JavaScript React
```

### output 2
```
-1
```

