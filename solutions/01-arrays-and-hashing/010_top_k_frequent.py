"""
문제: Top K Frequent Elements — 빈도 상위 k개 원소 반환
출처: LeetCode 347
난이도: Medium
카테고리: 배열 & 해싱
핵심 패턴: Counter + most_common(k) (Top-K 빈도 추출)
시간 복잡도: O(N + U log k)
공간 복잡도: O(U), U=고유 원소 수
"""

from collections import Counter
from typing import List
import heapq


# 가장 단순 — Counter.most_common(k) 한 줄
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Counter.most_common(k): 빈도 내림차순으로 (원소, 빈도) 튜플 k개 반환
    # 좌변 언패킹으로 값만 추출, 빈도는 _로 버린다
    return [value for value, _ in Counter(nums).most_common(k)]


# 힙 직접 사용 — most_common(k) 내부 구현과 동일
def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    # heapq.nlargest(k, iterable, key): key 기준 상위 k개 원소 반환
    return heapq.nlargest(k, counts, key=counts.get)


# 버킷 정렬 — O(N) 최적 (빈도 ≤ N 사실 활용)
def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    # 빈도를 인덱스로 사용 (최대 빈도 = len(nums))
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    # 빈도 큰 쪽부터 k개 채울 때까지 수집
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    for fn in (top_k_frequent, top_k_frequent_heap, top_k_frequent_bucket):
        assert sorted(fn([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
        assert fn([1], 1) == [1]
        assert fn([4, 4, 4, -1, -1, 2, 2, 2, 2], 1) == [2]
    print("모든 테스트 통과")
