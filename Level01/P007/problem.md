---
title: "초코의 특정 문자 세기"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
호기심 많은 강아지 **'초코'** 는 문장 속에 숨어 있는 특정 알파벳을 찾는 놀이를 좋아합니다.

**'초코'** 가 찾으려고 하는 **알파벳 한 개**와 **긴 문장**이 주어졌을 때, 그 문장 안에 해당 알파벳이 총 몇 번 등장하는지 세어보는 프로그램을 작성하세요.

(단, 대문자와 소문자는 서로 다른 문자로 취급합니다.)



## input_description
- 첫 번째 줄에 찾으려는 **알파벳 한 글자** $C$가 주어집니다.
- 두 번째 줄에 검색 대상이 되는 **문장** $S$가 주어집니다. (길이는 1000 이하, 공백 포함)

## output_description
- 문장 $S$ 안에 알파벳 $C$가 몇 번 포함되어 있는지 정수로 출력합니다.

# samples

### input 1
```
a
Banana and Apple
```

### output 1
```
4
```

### input 2
```
P
pineapple
```

### output 2
```
0
```

