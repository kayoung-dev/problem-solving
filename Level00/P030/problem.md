---
title: "오염된 데이터 복구"
level: "0"
time_limit: 1000
memory_limit: 128
languages: ["c", "cpp", "java", "js", "go", "python"]
tags: ["String"]
---

## description
서버실의 정전 사고로 인해 데이터베이스의 파일명들이 손상되었습니다.<br/>
시스템 관리자 '현우'는 백업 시스템에서 파일 리스트를 복구했지만, 불필요한 임시 파일들이 섞여 있습니다.<br/>
현우는 다음 규칙을 적용하여 중요한 파일만 필터링하고 표준 형식으로 변환하려 합니다.
1. **검색 조건 1:** 파일명이 특정 접두사 **prefix**로 시작해야 합니다.
2. **검색 조건 2:** 파일명의 길이가 **min_len**보다 **커야(초과)** 합니다. (같으면 안 됩니다.)
3. **변환 규칙:** 위 두 조건을 만족하는 파일명은 모두 **대문자**로 변환합니다.
4. **정렬:** 변환된 파일명 목록은 **사전 순(오름차순)**으로 정렬합니다.
5. **예외 처리:** 조건을 만족하는 파일이 하나도 없다면 **-1**을 출력합니다.
파일 리스트와 검색 조건이 주어졌을 때, 복구된 파일 목록을 출력하는 프로그램을 작성하세요.

## input_description
- 첫 번째 줄에 검색할 접두사 prefix와 기준 길이 min_len이 공백으로 구분되어 주어집니다.
  - prefix는 영문 소문자로 구성됩니다.
  - min_len은 1 이상 50 이하의 자연수입니다.
- 두 번째 줄에 공백으로 구분된 $N$개의 파일명(문자열)들이 주어집니다. ($1 \le N \le 100$)

## output_description
- 조건을 만족하는 파일명을 대문자로 변환하여 오름차순으로 정렬한 뒤 공백으로 구분해 출력합니다.
- 만족하는 파일이 없다면 -1을 출력합니다.

# samples

### input 1
```
sys 5
system sysfile autoexec sys config systematic
```

### output 1
```
SYSTEM SYSTEMATIC SYSFILE
```


### input 2
```
temp 10
tempfile template temporary
```

### output 2
```
-1
```
