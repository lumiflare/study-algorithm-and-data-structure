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
