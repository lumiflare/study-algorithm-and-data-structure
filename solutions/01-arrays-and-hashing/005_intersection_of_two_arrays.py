"""
문제: 두 배열의 교집합 (Intersection of Two Arrays)
출처: LeetCode 349
난이도: Medium
카테고리: 배열 & 해싱
핵심 패턴: set 교집합 연산자 (&) + sorted()
시간 복잡도: O(N + M + K log K)  (K=교집합 크기)
공간 복잡도: O(N + M)
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # set 변환: 중복 자동 제거 + O(1) 멤버십
    # & 연산자: 교집합을 한 번에
    # sorted(): set → 오름차순 list (출력 명세 충족)
    return sorted(set(nums1) & set(nums2))


# 메모리 미세 최적화: 작은 쪽만 set으로 만들고 큰 쪽은 그대로 활용
def intersection_optimized(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    small = set(nums1)
    # 큰 배열을 순회하며 small에 있는 것만 추출
    return sorted({x for x in nums2 if x in small})


if __name__ == "__main__":
    assert intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert intersection([1, 2, 3], [4, 5, 6]) == []
    assert intersection([1], [1]) == [1]
    print("모든 테스트 통과")
