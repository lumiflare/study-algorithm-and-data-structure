"""
문제: Two Sum (합이 target이 되는 두 인덱스)
출처: LeetCode 1
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 해시맵 1-패스 (조회→기록 순서로 자기 매칭 방지)
시간 복잡도: O(N)
공간 복잡도: O(N)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # seen: {원소값: 인덱스} — 과거에 본 원소들을 점진적으로 누적
    seen = {}
    for i, x in enumerate(nums):
        # 조회가 먼저: "내 짝꿍(target-x)을 이미 본 적 있나?"
        if target - x in seen:
            return [seen[target - x], i]
        # 기록은 나중: 자기 자신과 매칭되는 것을 자연스럽게 방지
        seen[x] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]           # 자기 매칭 회피
    assert two_sum([3, 3], 6) == [0, 1]              # 중복 보존
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]   # 음수 OK
    print("모든 테스트 통과")
