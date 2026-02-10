---
title: "소연의 암호 토큰 복원"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
보안 담당 소연은 출입 시스템 로그에서 암호 토큰을 복원하고 있습니다.<br/>
로그에는 같은 문자들이 반복해서 섞여 들어가는데, 소연이 필요한 토큰은 다음 규칙으로 복원됩니다.<br/>
문자열이 주어질 때, 중복된 문자를 제거하고 각 문자가 처음 등장한 순서대로 한 번씩만 남깁니다.<br/>
주어진 문자열을 위 규칙대로 변환하여 출력하는 프로그램을 작성하세요.

## input_description
- 한 줄에 문자열 S가 주어집니다.
- 문자열 길이는 1 이상 100 이하입니다.
- 문자열은 알파벳 대소문자와 숫자로만 이루어져 있습니다.

## output_description
- 중복 문자를 제거한 결과 문자열을 출력합니다.
- 문자의 순서는 처음 등장한 순서를 유지해야 합니다.

# samples

### input 1
```
ABBCDAA
```

### output 1
```
ABCD
```


### input 2
```
a1a1B2B2
```

### output 2
```
a1B2
```
