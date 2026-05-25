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
