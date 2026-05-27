# 배열 & 해싱 (Arrays & Hashing)

> 학습한 내용이 여기에 축적됩니다.

---

## 해시맵 (HashMap/Dictionary) [학습중 2026-05-24]

### 핵심 정리

1. **원리**: 키 → 해시 함수 → 인덱스 → 값 저장/조회 O(1)
2. **충돌**: 서로 다른 키가 같은 인덱스 → 체이닝으로 해결 (실전에서는 거의 O(1))
3. **조회/삽입/삭제/존재확인**: 모두 O(1) (배열의 O(N) 대비 압도적)
4. **키 제약**: list/set/dict는 키 불가 → tuple로 변환

### 실전 필수 패턴
```python
# 빈도수 세기
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
# 또는: freq = Counter(arr)

# Two Sum — O(N²) → O(N)
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i

# 그룹핑
groups = defaultdict(list)
for x in data:
    groups[key(x)].append(x)
```

---

## 해시셋 (HashSet) [학습중 2026-05-25]

### 핵심 정리

1. **용도**: "존재 여부"만 O(1)로 판정 (값 저장 불요). dict의 key-only 버전
2. **복잡도**: 삽입/삭제/`in` 모두 평균 O(1). 집합 연산 `&`, `|`, `-`, `^`
3. **빈 set은 `set()`** — `{}`는 dict (입문 최대 함정)
4. **원소는 hashable** — list 불가, tuple/frozenset OK
5. **순서 보장 X** — 순서 보존 중복 제거는 `dict.fromkeys(arr)`

### 실전 필수 패턴
```python
# 중복 판정
if len(set(arr)) != len(arr): ...

# 방문 체크 (BFS/DFS)
visited = set()
visited.add((r, c))   # 2D 좌표는 tuple로

# 두 컬렉션의 공통/차집합
common = set(a) & set(b)
only_a = set(a) - set(b)

# Longest Consecutive — O(N)
s = set(nums)
for n in s:
    if n - 1 not in s:   # 시작점만 검사
        k = 1
        while n + k in s: k += 1
```

### dict vs set 선택 기준
- **값이 필요하다** (인덱스/카운트/그룹) → **dict**
- **존재 여부만 필요하다** (방문/중복/멤버십) → **set**

---

## 빈도수 세기 (Frequency Count) [학습중 2026-05-25]

### 핵심 정리

1. **정석은 `Counter`** — 한 줄로 집계, 없는 키도 0 반환 (KeyError X)
2. **세 가지 카운트 패턴**: `if-else` / `dict.get(x, 0)+1` / `defaultdict(int)`
3. **최빈값**: `Counter(arr).most_common(K)` — 빈도 내림차순 K개
4. **값 범위가 작은 정수**: `freq = [0]*M` 배열 카운트가 dict보다 빠름
5. **Counter 산술**: `+`(빈도 합), `-`(빼기, 음수 제거), `&`(min), `|`(max)

### 실전 필수 패턴
```python
from collections import Counter

freq = Counter(arr)
freq.most_common(1)[0]            # 최빈값 한 개
freq['없는키']                     # 0 (안전)
[k for k,v in freq.items() if v==1]   # 유일 원소들

# 아나그램 판별 — 한 줄
Counter(s) == Counter(t)

# 첫 유일 문자 인덱스 (LeetCode 387)
freq = Counter(s)
for i, c in enumerate(s):
    if freq[c] == 1: return i
```

### 패턴 인식 트리거
"가장 많이 / K번 이상 / 빈도수 / 중복 횟수 / 한 번만 등장" → **즉시 Counter**

---

## 투 섬 패턴 (Two Sum Pattern) [학습중 2026-05-25]

### 핵심 정리

1. **발상 전환**: "모든 쌍 검사" → "내 짝꿍(target-x)이 이미 본 적 있나?"
2. **O(N²) → O(N)**: 해시맵의 O(1) 조회 덕분
3. **1-패스 패턴**: 조회 → 기록 순서 (자기 자신과 매칭 방지)
4. **인덱스 vs 값**: 명세 확인 필수
5. **정렬된 배열이라면** 투 포인터 대안 (공간 O(1))

### 실전 필수 패턴 (외워야 할 5줄)
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:           # 조회가 먼저
            return [seen[target - x], i]
        seen[x] = i                       # 기록은 나중
    return []
```

### 변형 모음
```python
# 쌍 존재 여부 (boolean)
seen = set()
for x in nums:
    if target - x in seen: return True
    seen.add(x)

# 차이가 K인 쌍
if x + k in seen or x - k in seen: ...

# 부분 배열 합 = K (prefix sum + Two Sum)
sums = {0: 1}; prefix = 0
for x in nums:
    prefix += x
    count += sums.get(prefix - k, 0)
    sums[prefix] = sums.get(prefix, 0) + 1
```

### 패턴 인식 트리거
"두 수의 합 / 차이가 K / 두 인덱스 / 부분 배열 합" → **즉시 Two Sum**

### 자주 하는 실수
- `seen[x] = i`를 조회보다 먼저 두면 자기 자신과 매칭됨 → **조회 → 기록 순서**
- 반환 형식 (인덱스 vs 값, 순서) — 출력 체크리스트 필수

---

## 프리픽스 합 (Prefix Sum) [학습중 2026-05-27]

### 핵심 정리

1. **누적합 한 번 계산 → 임의 구간 합 O(1)**. 전처리 O(N), 쿼리 O(1)
2. **`prefix[0] = 0` 더미 첫 칸**: 길이 N+1로 만들어 인덱스 분기 제거
3. **공식**: `nums[L..R] 합 = prefix[R+1] - prefix[L]`
4. **`accumulate(nums, initial=0)`** — 한 줄로 끝 (Python 3.8+)
5. **Subarray Sum = K 패턴**: 「현재 누적합 - K가 이전에 본 적 있나?」 → Two Sum 쌍둥이
6. **2D 프리픽스**: 포함-배제 원리, 직사각형 영역 합도 O(1)
7. **차분 배열**: 역방향 응용. 「구간 업데이트 여러 번 + 최종 배열」을 O(N+Q)에

### 실전 필수 패턴 (외워야 할 두 줄)
```python
from itertools import accumulate
from collections import defaultdict

# 1D 구간 합 — O(1) 쿼리
prefix = list(accumulate(nums, initial=0))
range_sum = prefix[R+1] - prefix[L]       # nums[L..R] 양 끝 포함

# Subarray Sum = K — 부분 배열 합이 K인 개수 (LeetCode 560)
prefix_count = defaultdict(int)
prefix_count[0] = 1                       # ⚠️ 초기화 필수 ("빈 합 = 0번 본 적 있음")
prefix = count = 0
for x in nums:
    prefix += x
    count += prefix_count[prefix - k]     # 조회 먼저 (Two Sum 패턴)
    prefix_count[prefix] += 1             # 기록 나중
```

### 2D 프리픽스 (행렬 직사각형 합 O(1))
```python
# 빌드: P[i+1][j+1] = grid[i][j] + P[i][j+1] + P[i+1][j] - P[i][j]
# 쿼리: rect = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

### 차분 배열 (Difference Array — 역방향 응용)
```python
# 여러 구간 [L,R]에 v를 더한 후 최종 배열을 구하는 문제
diff = [0] * (N + 1)
for L, R, v in updates:
    diff[L] += v
    diff[R+1] -= v
result = list(accumulate(diff[:-1]))      # 마지막 한 번 누적합
```

### 패턴 인식 트리거
- 「구간 합 / 부분 배열 합」 → 1D 프리픽스
- 「합 = K 인 부분 배열의 개수」 → 프리픽스 + 해시맵 (Two Sum 패턴)
- 「쿼리 여러 번」 → 전처리로 O(1) 응답
- 「행렬 직사각형 영역 합」 → 2D 프리픽스
- 「여러 구간 업데이트 후 최종 배열」 → 차분 배열

### 자주 하는 실수
- **`prefix_count[0] = 1` 초기화 누락** — 처음부터의 부분 배열 카운트 빠짐
- **인덱스 오프셋**: `prefix[R+1] - prefix[L]` (R 양 끝 포함). `prefix[R] - prefix[L]`로 쓰면 마지막 원소 빠짐
- **2D 포함-배제 부호**: 빼는 것 2개, 모서리 한 번 더 빼졌으니 다시 더하기
- **매 쿼리마다 `sum(nums[L:R+1])`** 호출 → O(N×Q) TLE. 전처리 필수
