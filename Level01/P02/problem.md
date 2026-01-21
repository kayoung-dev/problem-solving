# 인터넷 브라우저의 '뒤로 가기' (Browser Back Button)

## 문제 설명
평소 인터넷 쇼핑을 즐기는 '지수'는 마음에 드는 옷을 찾기 위해 여러 페이지를 돌아다닙니다. 쇼핑몰 사이트는 복잡해서 페이지를 자주 이동하게 됩니다.

브라우저의 **'뒤로 가기'** 버튼은 가장 최근에 방문한 페이지를 현재 기록에서 삭제하고, 바로 직전 페이지를 보여주는 기능을 합니다. 이는 자료구조의 **스택(Stack)** 개념인 **후입선출(LIFO)** 방식과 동일합니다.

초기 상태는 어떤 페이지도 방문하지 않은 **'HOME'** 상태입니다.
지수가 내린 명령어 리스트를 입력받아, 각 행동에 따른 결과를 출력하는 프로그램을 작성하세요.


---

## 입력 형식 (Input Format)
* 첫 번째 줄에 명령어의 개수 $N$이 주어집니다. ($1 \le N \le 100$)
* 두 번째 줄부터 $N$개의 줄에 걸쳐 명령어가 주어집니다.
    * `visit [URL]`: 해당 URL 페이지를 방문합니다. (URL은 공백 없는 문자열)
    * `back`: 현재 페이지를 닫고 이전 페이지로 돌아갑니다.
    * `current`: 현재 머물고 있는 페이지를 확인합니다.

## 출력 형식 (Output Format)
* `visit`: 방문 시 `[V] {URL}`을 출력합니다.
* `back`: 
    * 이전 페이지로 돌아갔다면 `[B] {현재_URL}`을 출력합니다. 
    * 돌아가서 홈 화면이 되었다면 `[B] HOME`을 출력합니다.
    * 이미 홈 화면이라서 돌아갈 곳이 없다면 `[B] IGNORED`를 출력합니다.
* `current`: 
    * 현재 페이지가 있다면 해당 URL을 출력합니다.
    * 홈 화면이라면 `HOME`을 출력합니다.

---
## 입출력 예시 (Sample I/O)

### 예시 1
**Input:**
```
5
visit naver.com
visit google.com
back
visit github.com
current
```
**Output:**
```
[V] naver.com
[V] google.com
[B] naver.com
[V] github.com
github.com
```

### 예시 2
**Input:**
```
4
visit blog.me
back
back
current
```
**Output:**
```
[V] blog.me
[B] HOME
[B] IGNORED
HOME
```
*  `blog.me`를 방문했다가 `back`을 하여 초기 상태(HOME)로 돌아왔습니다. 그 상태에서 다시 `back`을 시도했으나, 더 이상 돌아갈 페이지가 없어 명령이 무시(`IGNORED`)되었고, 현재 상태는 여전히 `HOME`입니다.
