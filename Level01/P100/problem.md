# 릴리즈 노트 정리하기

## 문제 설명
팀 리더 **지훈**은 새로운 버전을 배포하기 전에 Git 커밋 로그를 정리하여 릴리즈 노트를 작성하려고 합니다.

커밋 로그에는 실제 기능 개발과 관련 없는 기록도 함께 섞여 있기 때문에,  
지훈은 모든 커밋을 그대로 사용하지 않고 **릴리즈 노트에 적합한 커밋만 골라 정리**합니다.

각 커밋은 커밋 해시, 커밋 시간, 그리고 한 줄의 커밋 메시지로 이루어져 있으며,  
메시지는 보통 `type(scope): 내용` 또는 `type: 내용` 형태로 작성됩니다.  
이때 `type`은 커밋의 성격을 나타내며, `scope`는 변경이 적용된 영역을 의미합니다.

지훈은 릴리즈 노트에 필요한 커밋만 골라 아래 규칙으로 정렬해 출력합니다.
- 메시지가 `Merge`로 시작하는 커밋은 제외합니다.
- 메시지가 `docs:`로 시작하는 커밋은 제외합니다.
- `type` 우선순위: `fix` → `feat` → `refactor` → `test` → `chore`
- 같은 `type`이면 `scope`이 있는 커밋이 먼저 오고, 그 안에서 사전순으로 정렬합니다.
- 같은 `type`과 `scope`이면 커밋 시간을 **최신이 먼저** 오도록 정렬합니다.
- 그래도 같으면 해시를 사전순으로 정렬합니다.

정리된 결과는 커밋 메시지를 기반으로 한 간결한 형태로 출력하며,  
변경 범위가 없는 경우에는 범위를 생략하여 표시합니다.

주어진 Git 커밋 로그를 분석하여,  
지훈이 릴리즈 노트에 정리하게 될 커밋 목록을 순서대로 출력하세요.

---
## 입력 형식 (Input Format)
- 첫 줄에는 커밋의 개수 N이 주어집니다.  
- 이후 N줄에 걸쳐 각 줄마다 하나의 커밋 로그가 주어지며,  
- 각 로그는 `커밋해시 날짜 시간 메시지`의 순서로 구성됩니다.  
- 메시지는 공백을 포함할 수 있으며, 줄 끝까지가 하나의 메시지로 간주됩니다.

---

## 출력 형식 (Output Format)
- 릴리즈 노트에 포함되는 커밋만을 조건에 맞게 정렬하여,  
각 커밋을 한 줄씩 출력합니다.  
- 출력 형식은 `type(scope): 내용` 또는 `type: 내용`입니다.

---

## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
```
7
a1b2c3d4 2026-01-05 09:10 feat(api): add search endpoint
ff00aa11 2026-01-05 10:00 fix(api): handle null request
1234abcd 2026-01-05 08:30 docs: update README
beefcafe 2026-01-04 22:00 refactor(core): split service layer
0badf00d 2026-01-05 10:00 fix: patch build error
abcd0001 2026-01-03 12:00 Merge branch 'dev'
9999eeee 2026-01-05 09:50 chore(ci): update pipeline
```
**Output:**
```
fix(api): handle null request
fix: patch build error
feat(api): add search endpoint
refactor(core): split service layer
chore(ci): update pipeline
```
- `docs:`와 `Merge ...` 커밋은 제외됩니다.
- `fix`가 가장 먼저 나오고, 같은 `fix`에서는 scope가 있는 것이 먼저 정렬됩니다.

### 예시 2
**Input:**
```
5
aa11bb22 2026-01-01 10:00 feat: init project
cc33dd44 2026-01-01 10:01 feat(ui): add button
ee55ff66 2026-01-01 09:59 fix(ui): hotfix
11223344 2026-01-01 10:02 fix: adjust config
deadbeef 2026-01-01 10:03 test(ui): add tests
```
**Output:**
```
fix(ui): hotfix
fix: adjust config
feat(ui): add button
feat: init project
test(ui): add tests
```
- 같은 type이면 scope 사전순, scope가 없는 항목은 같은 type에서 뒤로 갑니다.
- 같은 type+scope라면 시간이 최신인 커밋이 먼저 옵니다.

### 예시 3
**Input:**
```
2
abcd1234 2026-01-01 00:00 chore: setup
bead5678 2026-01-01 00:01 docs: note
```
**Output:**
```
chore: setup
```
