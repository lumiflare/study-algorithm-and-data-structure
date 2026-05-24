# Python 기초 (코딩테스트용)

> Phase 1 (Week 1) 사전 지식

---

## A. 변수, 조건문, 반복문 [학습완료 2026-05-24]

### 핵심 정리

1. **자료형**: `int`(크기 무제한!), `float`, `str`, `bool`
2. **정수 나눗셈**: `//`는 항상 내림 → `-7 // 2 = -4` (주의)
3. **조건 체이닝**: `0 <= x < n` 가능 (Python 전용)
4. **range**: `range(n)` = 0~n-1, `range(a,b)` = a~b-1 (끝 미포함)
5. **enumerate**: 인덱스+값 동시에 → `for i, v in enumerate(arr)`
6. **in 연산자**: `in set/dict` = O(1), `in list` = O(N)
7. **break/continue**: break=루프 탈출, continue=이번 회차 건너뛰기

### 빈출 패턴
```python
# 격자 범위 체크
if 0 <= x < n and 0 <= y < m:

# 삼항 연산자
result = "짝수" if n % 2 == 0 else "홀수"

# enumerate 활용
for i, val in enumerate(arr):
```

---

## B. Python 내장 자료구조 [학습완료 2026-05-24]

### 핵심 정리

1. **list**: 순서O, 중복O, 변경O — 인덱싱 O(1), `in` O(N), `append/pop` O(1)
2. **dict**: 키:값, `in` O(1) — `Counter`, `defaultdict(list/int)` 필수 암기
3. **set**: 중복X, 순서X, `in` O(1) — 방문 체크, 중복 제거용
4. **tuple**: 불변 — dict 키/set 원소로 사용 가능 (좌표 표현)
5. **2D 배열 함정**: `[[0]*m]*n` ❌ → `[[0]*m for _ in range(n)]` ✅
6. **빈 set 생성**: `{}` 는 dict! → `set()` 사용
7. **성능 핵심**: `in list` O(N) vs `in set` O(1) → TLE 방지의 핵심

### 빈출 패턴
```python
# 빈도수 세기
from collections import Counter
freq = Counter(arr)

# 그래프 인접 리스트
from collections import defaultdict
graph = defaultdict(list)

# 중복 판별
len(arr) != len(set(arr))

# 좌표 방문 체크
visited = set()
visited.add((x, y))
```

## C. 함수 & 재귀 기초 [학습완료 2026-05-24]

### 핵심 정리

1. **함수 구조**: `def 이름(인자): ... return 결과`
2. **여러 값 반환**: `return a, b` → 튜플, `x, y = func()`로 언패킹
3. **스코프**: 지역 변수와 전역 변수는 별개. 리스트/딕셔너리는 참조라 내부 수정 가능
4. **재귀 필수 2요소**: 기저 조건 (멈추기) + 재귀 호출 (작게 만들기)
5. **호출 스택**: 재귀마다 스택에 쌓이고, return하면 꺼냄
6. **재귀 깊이**: 기본 1000 → `sys.setrecursionlimit(10**6)` 설정
7. **단순 재귀 피보나치는 O(2^N)**: → DP로 해결 (나중에 학습)

### 빈출 패턴
```python
import sys
sys.setrecursionlimit(10**6)  # DFS/트리 문제 필수

# 재귀 템플릿
def solve(n):
    if 기저조건:
        return 값
    return 조합(solve(더_작은_문제))
```

## D. 코딩테스트 입출력 패턴 [학습완료 2026-05-24]

### 핵심 정리

1. **빠른 입력**: `import sys; input = sys.stdin.readline` — 항상 사용!
2. **정수 읽기**: `int(input())`, `map(int, input().split())`
3. **리스트 읽기**: `list(map(int, input().split()))`
4. **2D 격자**: `[list(map(int, input().split())) for _ in range(n)]`
5. **문자열 입력**: `.strip()` 으로 줄바꿈 제거
6. **출력**: `print(*arr)` = 공백 구분, 대량 출력은 `'\n'.join()`
7. **solve() 패턴**: 함수로 감싸면 return 조기 종료 + 속도 이점

### 실전 템플릿
```python
import sys
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # 풀이
    print(answer)

solve()
```

## E. 시간 복잡도 & 공간 복잡도 [학습완료 2026-05-24]

### 핵심 정리

1. **Big-O 규칙**: 상수 무시, 낮은 차수 무시, 최악 기준
2. **N 범위 → 알고리즘 선택**: N≤1,000 → O(N²), N≤100,000 → O(NlogN), N≤10M → O(N)
3. **Python은 느림**: 1초 ≈ 2,000만~5,000만 연산. C/Java 대비 3~5배
4. **숨겨진 O(N) 3대장**: `in list`, `s += c` (문자열), `list.pop(0)`
5. **해결법**: `in set` O(1), `''.join()` O(N), `deque.popleft()` O(1)
6. **공간**: int배열 ~900만개, 2D N×N은 N≈3,000까지

### N 범위 → 복잡도 표 (암기!)
```
N ≤ 10     → O(N!)       완전탐색
N ≤ 20     → O(2^N)      비트마스킹
N ≤ 100    → O(N³)       플로이드
N ≤ 1,000  → O(N²)       DP, 이중루프
N ≤ 100K   → O(NlogN)    정렬, 이진탐색
N ≤ 10M    → O(N)        투포인터, 해시
```
