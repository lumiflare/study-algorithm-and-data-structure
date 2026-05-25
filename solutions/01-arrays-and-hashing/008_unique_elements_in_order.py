"""
문제: 유일 원소를 원본 순서대로 (Unique Elements in Order)
출처: 자체 출제
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 2-패스 (Counter 빈도 집계 + 원본 nums 순회로 순서 보장)
시간 복잡도: O(N)
공간 복잡도: O(U)
"""

from collections import Counter


# 풀이 A: 정석 2-패스 + 리스트 컴프리헨션 (가장 우아)
def unique_elements(nums: list[int]) -> list[int]:
    # 1패스: 전체 빈도를 미리 집계
    freq = Counter(nums)
    # 2패스: 원본 nums를 순회 → 순서 자동 보장 → 빈도 1만 골라 누적
    return [x for x in nums if freq[x] == 1]


# 풀이 B: 명시적 루프 (학습용 — 동작이 더 잘 보임)
def unique_elements_loop(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    result = []
    for x in nums:               # 원본 nums를 순회 → 순서 보장
        if freq[x] == 1:
            result.append(x)
    return result


# 풀이 C: items() 활용 (Counter의 삽입 순서를 신뢰 — 의도 불명확하므로 비추천)
def unique_elements_items(nums: list[int]) -> list[int]:
    counts = Counter(nums)
    result = []
    for num, count in counts.items():    # 변수명을 num, count로 → 의미 명확
        if count == 1:
            result.append(num)            # num을 append (count가 아님)
    return result


if __name__ == "__main__":
    for fn in (unique_elements, unique_elements_loop, unique_elements_items):
        assert fn([1, 2, 3, 2, 4, 1, 5]) == [3, 4, 5]
        assert fn([1, 1, 2, 2]) == []
        assert fn([7]) == [7]
        assert fn([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    print("모든 테스트 통과")
