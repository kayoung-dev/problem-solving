---
title: "외계 신호 압축 해제"
level: "1"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["Stack", "String"]
---

## description
우주 탐사선 **나로호**는 먼 외계 행성으로부터 의문의 신호를 수신했습니다.<br/>
분석 결과, 이 신호는 저장 공간을 아끼기 위해 특정 규칙으로 압축되어 있었습니다.<br/>
압축된 신호의 규칙은 $k[string]$ 형태입니다. 대괄호($[]$) 안에 있는 $string$ 내용을 $k$번 반복한다는 의미이며, $k$는 $1$ 이상의 양의 정수입니다. 이 규칙은 중첩되어 나타날 수도 있습니다.<br/>
예: `3[a]2[bc]`는 `aaabcbc`로, `3[a2[c]]`는 `accaccacc`로, `2[abc]3[cd]ef`는 `abcabccdcdef`로 복원됩니다.<br/>
수신된 압축 신호 $S$가 주어질 때, 이를 원래의 문장으로 복원하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 압축된 신호 문자열 $S$가 주어집니다.
- 문자열 $S$의 길이는 $1$ 이상 $1,000$ 이하입니다.
- 숫자는 $k$를 의미하며, $1$ 이상 $300$ 이하의 정수입니다. 문자열은 알파벳 소문자로만 구성됩니다.
- 모든 입력은 항상 올바른 압축 형식을 따릅니다.

## output_description
- 압축을 해제한 원래의 문자열을 출력합니다.

# samples

### input 1
```
3[a]2[bc]
```

### output 1
```
aaabcbc
```


### input 2
```
3[a2[c]]
```

### output 2
```
accaccacc
```
