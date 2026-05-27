"""
문제: Range Sum Query - Immutable — 클래스로 구간 합 쿼리
출처: LeetCode 303
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 1D 프리픽스 합 (전처리 O(N) + 쿼리 O(1))
시간 복잡도: O(N) 전처리, O(1) per 쿼리
공간 복잡도: O(N)
"""

from typing import List
from itertools import accumulate


# A) 직접 루프 — 학습 단계에서 가장 직관적
class NumArray:
    def __init__(self, nums: List[int]):
        # 길이 N+1로 미리 메모리 확보 — 괄호 (N+1) 꼭 묶기
        prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
        # 루프 종료 후 한 번만 인스턴스 속성에 저장
        self.prefix = prefix

    def sum_range(self, left: int, right: int) -> int:
        # 양 끝 포함 구간 합: prefix[right+1] - prefix[left]
        # 다른 메서드이므로 prefix 참조에 self. 필수
        return self.prefix[right + 1] - self.prefix[left]


# B) accumulate 한 줄 풀이 — Pythonic
class NumArrayPythonic:
    def __init__(self, nums: List[int]):
        # initial=0 → 첫 칸 0이 들어간 길이 N+1 누적합 배열
        self.prefix = list(accumulate(nums, initial=0))

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    for Cls in (NumArray, NumArrayPythonic):
        na = Cls([-2, 0, 3, -5, 2, -1])
        assert na.sum_range(0, 2) == 1
        assert na.sum_range(2, 5) == -1
        assert na.sum_range(0, 5) == -3
        # 단일 원소 / 경계
        na2 = Cls([1, 2, 3, 4, 5])
        assert na2.sum_range(0, 0) == 1     # 첫 원소만
        assert na2.sum_range(4, 4) == 5     # 마지막 원소만
        assert na2.sum_range(0, 4) == 15    # 전체
    print("모든 테스트 통과")
