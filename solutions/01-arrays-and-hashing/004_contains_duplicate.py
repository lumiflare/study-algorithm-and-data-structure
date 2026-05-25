"""
문제: 중복 원소 판정 (Contains Duplicate)
출처: LeetCode 217
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 해시셋 + early return
시간 복잡도: O(N)
공간 복잡도: O(N)
"""


def has_duplicate(nums: list[int]) -> bool:
    # 본 적 있는 값을 누적하는 해시셋
    visited = set()
    for value in nums:
        # O(1) 멤버십 조회 — list로 하면 O(N)이라 시간 초과
        if value in visited:
            return True
        visited.add(value)
    return False


# 한 줄 풀이 (참고용)
# 항상 전체를 순회하므로 early return보다 평균적으로 느릴 수 있음
def has_duplicate_oneliner(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3, 4]) is False
    assert has_duplicate([1]) is False
    assert has_duplicate([]) is False
    assert has_duplicate([1, 1]) is True
    print("모든 테스트 통과")
