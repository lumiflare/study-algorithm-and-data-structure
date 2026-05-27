# 오답 노트

> 틀린 문제를 기록하고, 같은 실수를 반복하지 않기 위한 노트입니다.
> 포맷: `docs/records.md` 참조

---

<!-- 오답 기록은 아래에 추가됩니다 -->

## 2026-05-25 [배열 & 해싱]
- **문제**: 두 배열의 교집합 — 중복 없는 오름차순 **정렬 리스트** 반환
- **오답**: `return set(nums1) & set(nums2)` — set을 그대로 반환
- **정답**: `return sorted(set(nums1) & set(nums2))` — sorted()로 list 변환 + 정렬
- **실패 원인**: 알고리즘(set 교집합)은 정확했으나, **출력 명세(list, 오름차순)를 누락**. set은 순서 보장 X, 타입도 list 아님
- **핵심 교훈**: 출력 타입·정렬 요구·중복 처리·빈 결과 표현 — 4가지를 코드 작성 전 반드시 확인할 것. `sorted()`는 list 반환 + 정렬을 한 번에 해결

## 2026-05-25 [배열 & 해싱]
- **문제**: 최빈 문자 + 동점 시 알파벳 순 — `(문자, 횟수)` 튜플 반환
- **오답**:
  ```python
  s_arr = sort(s.split())                    # sort 함수 없음 (NameError)
  return Counter(s_arr).most_common(1)       # list of tuple 반환 (튜플 아님)
  ```
- **정답**:
  ```python
  return Counter(sorted(s)).most_common(1)[0]
  # 또는 명시적 key 함수:
  freq = Counter(s)
  ch = min(freq, key=lambda c: (-freq[c], c))
  return (ch, freq[ch])
  ```
- **실패 원인**:
  1. `sort()`는 함수가 아닌 메서드 → `sorted()` 사용해야 함
  2. `"abc".split()`은 공백 분리 → 문자 분리는 `list(s)` 또는 그냥 `s` 전달
  3. `most_common(1)`은 list 반환 → `[0]`으로 튜플 추출 필요 (이전 교집합 문제와 동일한 출력 타입 미준수)
- **핵심 교훈**:
  - `sort` vs `sorted` 구분: **함수 = `sorted()`, 메서드 = `list.sort()`**
  - `most_common(1)`은 **항상 `[0]` 붙여서 튜플 꺼내기** — 손가락에 새길 것
  - 동점 처리는 **명시적 key 함수**로 작성: `key=lambda x: (-freq[x], x)` (빈도 내림차순, 사전순 오름차순)
  - 알고리즘 발상(사전 정렬 후 Counter)은 좋았음 — 구현만 실패

## 2026-05-25 [배열 & 해싱]
- **문제**: 첫 유일 문자의 인덱스 — 원본 문자열에서 딱 한 번 등장하는 첫 문자의 위치
- **오답**:
  ```python
  s_counts = Counter(sorted(list(s)))     # ❌ 정렬로 원본 위치 정보 파괴
  for index, value in enumerate(s_counts.values()):
      if s_counts[index] == 1 return index  # ❌ 콜론 누락 + 정수로 Counter 조회
  ```
- **정답**:
  ```python
  freq = Counter(s)                       # 1패스: 빈도 집계
  for i, c in enumerate(s):               # 2패스: 원본 순회
      if freq[c] == 1: return i
  return -1
  ```
- **실패 원인**:
  1. **이전 문제(최빈 문자)의 sorted+Counter 트릭을 잘못된 곳에 적용** — 이전엔 "문자 자체"가 답이라 정렬 OK였지만, 이번엔 "원본 위치"가 답이라 정렬 금지
  2. 문법: `if 조건 return X`에 콜론 누락
  3. `s_counts[index]` — 정수 0,1,2로 문자 키 Counter를 조회 (모두 0 반환 → 조건 항상 False)
- **핵심 교훈**:
  - **반환값이 "원본 위치"라면 원본 컨테이너를 절대 정렬/변형하지 말 것**
  - **2-패스 패턴**: 1패스 집계(Counter) + 2패스 원본 순회(`enumerate(s)`로 인덱스 획득)
  - "첫 번째 ___인 ___" 표현 보이면 2-패스 의심
  - Counter는 키 타입을 지킨다 — 문자 키는 `freq['c']`로, 정수로 조회하지 말기

✅ 극복 2026-05-26 (재출제 시 Counter + enumerate 2-패스로 정답. 초기 제출에서 `return value`(문자)를 반환하는 사소한 버그가 있었으나 피드백 1회로 즉시 수정. 알고리즘 패턴은 체화됨)

## 2026-05-25 [배열 & 해싱]
- **문제**: 유일 원소 목록을 원본 등장 순서대로 — list 반환
- **오답**:
  ```python
  for key, value in counts:                   # ❌ .items() 누락 → TypeError
      if counts[key] == 1:
          only_one_count_nums.append(value)   # ❌ value(빈도수)를 append (key였어야)
  ```
- **정답**:
  ```python
  freq = Counter(nums)
  return [x for x in nums if freq[x] == 1]   # 또는 .items()로 (k, v) 순회 후 k append
  ```
- **실패 원인**:
  1. **`.items()` 누락**: `for k, v in dict` 형태로는 키만 나옴 → 언패킹 실패
  2. **`key`와 `value`의 의미 혼동**: items()에서 `key=원소값`, `value=빈도수`. 결과에 넣어야 할 건 key였는데 value를 넣음 → `[1,1,1]` 반환
  3. 머릿속 트레이스를 했다면 즉시 발견 가능했던 실수
- **핵심 교훈**:
  - **`for k, v in dict.items():`** — `.items()`는 dict 순회의 표준 보일러플레이트, 손에 익히기
  - **`items()`의 의미**: k=원소(우리가 원하는 결과), v=빈도(조건 검사용). 변수명을 `num, count`로 쓰면 헷갈리지 않음
  - **순서 보장이 필요하면 원본을 순회** — Counter 순회 의존 X. `[x for x in nums if freq[x] == 1]`이 표준
  - **머릿속 트레이스 필수**: 코드 작성 후 예제 1개로 한 줄씩 따라가기 (1분 투자로 ❌ → ✅)

## 2026-05-25 [배열 & 해싱]
- **문제**: Two Sum — 합이 target인 두 원소의 인덱스 `[i, j]` 반환
- **오답**:
  ```python
  nums_dict = {v: i for i, v in enumerate(nums)}   # ❌ 미리 다 채움 → 중복 손실 + 자기 매칭
  for value, index in nums_dict.items():
      nums_dict.get(target - value) != None         # ❌ if 누락 + 평가만 함
         return [...]                                # ❌ IndentationError
  ```
- **정답** (정석 5줄, 1-패스):
  ```python
  seen = {}
  for i, x in enumerate(nums):
      if target - x in seen:
          return [seen[target - x], i]
      seen[x] = i
  return []
  ```
- **실패 원인**:
  1. **1-패스가 정답인데 2-패스로 풀이** — 미리 dict를 다 채우면 자기 매칭 + 중복 손실
  2. dict comprehension `{v:i for ...}`는 **같은 키 중복 시 마지막 값으로 덮어씀** → `[3,3]` 케이스에서 첫 3이 사라짐
  3. `if` 키워드 누락 — `nums_dict.get(...) != None`만으로는 단순 평가
  4. 들여쓰기 오류 → IndentationError
- **핵심 교훈**:
  - **"미리 다 채우지 말고 점진적으로"** — 조회→기록 순서가 자기 매칭을 막는 핵심
  - **5줄 패턴을 보지 않고 타이핑할 수 있어야 함** — 손에 박힌 것만 실전에서 나옴
  - dict comprehension은 **유니크 키일 때만** 안전 (Two Sum 같은 곳에 X)
  - `if`는 빼면 안 되는 키워드 — 단순 비교식만 쓰면 의미 없음

❌ 재도전 실패 2026-05-26 — 모범 답안을 본 후 24시간이 지나 다시 풀었으나, 순서를 거꾸로(`seen[num]=index` 먼저 → `if target-num in seen` 나중에) 작성하여 **3가지 버그 동시 발생**:
  1. 기록→조회 순서 역전 → 자기 매칭 발생 (`nums=[3,3], target=6` → `[0,0]`)
  2. `return [seen[num], index]` — `seen[num]`은 방금 저장한 자기 자신. 정답은 `seen[target-num]`
  3. 못 찾았을 때 반환 없음
  → 어제 교훈 "조회→기록"이 손에 박히지 않은 상태. **5줄 패턴 매일 백지 쓰기 1주일 권장**.

## 2026-05-26 [배열 & 해싱]
- **문제**: 정확히 2번 등장하는 원소를 **두 번째 등장 인덱스 기준 오름차순**으로 반환 (`[4,3,2,7,8,2,3,1]` → `[2,3]`)
- **오답**:
  ```python
  num_counts = Counter(nums)
  two_count_nums = list()
  for num, count in num_ounts.items():            # ❌ num_ounts (타이포)
    if count == 2: two_count_nums.append(num)
  result = list()
  for index, num in enumerate(nums):
    if num not in result & num in two_count_nums: # ❌ &는 비트 AND, list 멤버십 O(N)
        result.append(num)                         # ❌ 첫 등장 시점에 기록 → 순서 오류
  return result   # 실제 반환: [3,2] (기대: [2,3])
  ```
- **정답** (O(N), 5줄):
  ```python
  freq = Counter(nums)
  seen = set()
  result = []
  for x in nums:
      if freq[x] == 2 and x in seen:   # 두 번째 만남 = 두 번째 인덱스 시점
          result.append(x)              # 앞에서부터 순회하므로 자연 정렬됨
      seen.add(x)
  return result
  ```
- **실패 원인**:
  1. **타이포** (`num_ounts`) — NameError 즉시 실패
  2. **`&` ≠ `and`** — 비트 연산자 오용. `&`의 우선순위가 `in`보다 높아 `result & num`(list & int) → TypeError
  3. **list `in` = O(N)** — 멤버십 검사를 list로 두 번 → 전체 O(N²), N=10⁵에서 TLE
  4. **알고리즘 버그**: "두 번째 인덱스 기준 정렬"인데 **첫 등장 시점**에 기록 → `[3,2]` 반환
- **핵심 교훈**:
  - **`&` 비트 / `and` 논리** — 둘은 다른 연산자. 우선순위도 다름 (`&` > `in` > `and`)
  - **멤버십 검사는 set** — list `in`은 O(N), set/dict `in`은 O(1). "in 검색"이 보이면 set 후보
  - **"N 번째 등장" 시그널 → 그 시점에 기록** — 빈도만 보지 말고 등장 **순간**을 추적
  - **앞에서부터 순회 + 조건 만남 시 append** = 자연 정렬 (별도 sort 불필요한 케이스가 많음)
  - Counter `.items()` 활용 자체는 성공 — 지난 오답(items 누락)과 비교하면 한 단계 진보

## 2026-05-26 [배열 & 해싱]
- **문제**: Top K Frequent Elements — 빈도 상위 k개 원소 반환 (LeetCode 347)
- **오답**:
  ```python
  for tupple in counts.most_common()       # ❌ 콜론 누락 + most_common(k)이 아닌 most_common()
      value, count = tupple                # count 미사용
      result.append(value)
  return result   # 항상 전체 원소 반환 (k 매개변수 사용 안 함)
  ```
- **정답**:
  ```python
  return [value for value, _ in Counter(nums).most_common(k)]
  ```
- **실패 원인**:
  1. **`k`를 함수 본문에서 한 번도 사용 안 함** — 매개변수 받아놓고 안 쓴 채 제출 (강한 위험 신호)
  2. **`most_common()` 인자 누락**: `Counter.most_common(n)`에서 `n` 생략 시 **전체** 반환. 상위 k개만 원하면 `most_common(k)`
  3. 콜론(`:`) 누락 → SyntaxError (실행 전 확인 안 함을 시사)
  4. `tupple` 오타, `count` 사용 안 함
- **핵심 교훈**:
  - **매개변수 사용 체크**: 함수 본문에 `k`가 한 번도 안 나오면 99% 버그. 제출 전 "받은 인자 다 썼나?" 확인
  - **`most_common(k)` 시그니처 새기기**: 인자 없으면 O(N log N) 전체 정렬, 인자 있으면 O(N log k) 힙 사용 — 성능까지 다름
  - **언패킹은 좌변에서**: `for value, _ in counts.most_common(k):` 한 줄로 처리. 별도 `value, count = tupple` 불필요
  - **머릿속 트레이스 + 콜론 체크** — 어제 Two Sum의 `if` 누락과 같은 부류의 실수. 작성 후 1패스 실행을 습관화

✅ 극복 2026-05-26 (3회 제출 끝에 알고리즘+문법 모두 정답. `most_common(k)` 패턴 체화됨. 다만 1·2차 제출에서 콜론 누락 → 콜론 자리 `"` 오타가 연속 발생 — "작성 후 실행/트레이스 1회" 습관이 아직 미정착이라는 점은 추후 주의)

## 2026-05-27 [배열 & 해싱]
- **문제**: Valid Anagram — 두 문자열이 같은 문자 구성인가 (LeetCode 242)
- **오답**:
  ```python
  if len(s) != len(t): return false;          # ❌ false 소문자 → NameError
  return sorted(list(s)) == sorted(list(s))   # ❌ 두 번째 s는 t여야 함 (변수명 오타)
  ```
- **정답**:
  ```python
  # A) Counter 비교
  if len(s) != len(t): return False
  return Counter(s) == Counter(t)
  # B) 정렬 비교
  return sorted(s) == sorted(t)
  ```
- **실패 원인**:
  1. **언어 혼동**: `false` (JS/Java) → Python은 **`False`** (대문자 F). 다른 언어 경험이 섞임
  2. **변수명 오타**: `t`를 써야 할 자리에 `s`를 또 씀 → 항상 자기 자신과 비교 → 항상 True
  3. 알고리즘 발상(조기 종료 + Counter/정렬 두 가지)은 완벽했음. **구현 단계의 잔실수**
- **핵심 교훈**:
  - **Python 진릿값은 `True`/`False`** (대문자 시작) — `true`/`false`/`null` 같은 다른 언어 키워드 의식
  - **변수명 오타는 트레이스로만 잡힌다** — 예제 1개로 머릿속 변수 추적 1패스 필수
  - **메모(주석)로 사고를 외화한 건 매우 좋음** — 알고리즘 발상이 두 가지나 떠오른 건 강점
  - 오늘 세션 누적 잔실수 4건: 반환 타입 / 콜론 / `"` 오타 / 변수명 오타 — **작성 후 30초 트레이스 루틴** 정착 필요

✅ 극복 2026-05-27 (피드백 직후 본인이 두 버그(`false→False`, `sorted(s)==sorted(s)→sorted(t)`)를 정확히 수정. 네 예제 모두 통과. **외부 채점 없이 자력 수정에 성공한 첫 사례** — 「작성 후 30초 트레이스」 루틴이 의식적으로 작동하기 시작한 신호)

## 2026-05-27 [배열 & 해싱]
- **문제**: Range Sum Query - Immutable — 클래스로 구간 합 쿼리 (LeetCode 303)
- **오답**:
  ```python
  class NumArray:
    def __init__(self, nums):
      self.nums = nums
            prefix = list()            # ❌ 들여쓰기 깨짐
        prefix[0] = 0                  # ❌ 빈 리스트 인덱스 접근 → IndexError
        for index, num in enumerate(self.nums):
          prefix[index + 1] = prefix[index] + num  # ❌ 동일 문제
      self.prefix = prefix

    def sum_range(self, left, right)              # ❌ 콜론 누락
      return prefix[right - 1] - prefix[left]     # ❌ self. 누락 + right-1 (정답은 right+1)
  ```
- **정답**:
  ```python
  from itertools import accumulate
  class NumArray:
      def __init__(self, nums):
          self.prefix = list(accumulate(nums, initial=0))
      def sum_range(self, left, right):
          return self.prefix[right + 1] - self.prefix[left]
  ```
- **실패 원인**:
  1. **들여쓰기 4단계가 다르게 섞임** → IndentationError. 작성 후 들여쓰기 정렬 확인 안 함
  2. **빈 리스트에 `prefix[0] = 0`** — `list()` 는 빈 `[]`. 인덱스 대입은 불가. `[0]*(N+1)` 또는 `append` 또는 `accumulate` 사용해야
  3. **메서드 시그니처 콜론 누락** — 오늘 세션 콜론 누락 3번째
  4. **인덱스 오프셋**: `right - 1` (정답은 `right + 1`). 노트에 외운 공식 `prefix[R+1] - prefix[L]` 잊음
  5. **`self.` 누락** — 인스턴스 메서드 안에서 인스턴스 변수 접근에 `self.` 필수
- **핵심 교훈**:
  - **빈 리스트 인덱스 대입 불가** → `[0]*(N+1)` 로 미리 메모리 확보, 또는 `accumulate(nums, initial=0)` 한 줄
  - **「+1 / +0」 짝궁**: 오른쪽 끝은 `+1` (포함하려고), 왼쪽 끝은 그대로
  - **클래스 메서드 작성 시 `self.` 확인 루틴** 추가 — 인스턴스 변수는 모두 `self.xxx`
  - **들여쓰기는 한 단계 = 4 스페이스 (또는 일관 2)** — 섞이면 즉시 에러
  - 오늘 세션 누적 잔실수 5건 모두 같은 부류: **알고리즘 정확, 작성 후 트레이스 부재**. 다음 제출 전 30초 트레이스 의식적으로

✅ 극복 2026-05-27 (5회차 도전 끝에 정답. 매 회차마다 1~2개씩 잡으며 점진적 수정 — 1차:들여쓰기/콜론/self/오프셋 다수 → 2차:콜론·오프셋 잡음 → 3차:for 본문 들여쓰기 잡음 → 4차:self.prefix 참조 잡음 → 5차:괄호 `(N+1)` + self.prefix 대입 위치 = 완전 정답. **「한 번에 다 잡으려 하지 말고 회차마다 줄이기」 학습 패턴 정착**. 클래스 메서드의 self·들여쓰기·연산자 우선순위 4가지가 손에 박힘)
