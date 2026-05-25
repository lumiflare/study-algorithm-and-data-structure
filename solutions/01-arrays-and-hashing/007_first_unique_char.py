"""
문제: 첫 유일 문자의 인덱스 (First Unique Character in a String)
출처: LeetCode 387
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 2-패스 (Counter 빈도 집계 + 원본 순회로 위치 결정)
시간 복잡도: O(N)
공간 복잡도: O(U), U=유니크 문자 수 (알파벳이면 ≤26)
"""

from collections import Counter


def first_unique_char(s: str) -> int:
    # 1패스: 전체 빈도 집계 — 어떤 문자가 몇 번 등장하는지 미리 안다
    freq = Counter(s)
    # 2패스: 원본 순서대로 순회 — enumerate로 인덱스 직접 획득
    # 처음으로 빈도가 1인 문자를 만나면 그 인덱스가 답
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1


# 알파벳 한정 — 배열 카운트로 미세 최적화 (해시 오버헤드 제거)
def first_unique_char_array(s: str) -> int:
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    for i, c in enumerate(s):
        if cnt[ord(c) - ord('a')] == 1:
            return i
    return -1


if __name__ == "__main__":
    for fn in (first_unique_char, first_unique_char_array):
        assert fn("leetcode") == 0
        assert fn("loveleetcode") == 2
        assert fn("aabb") == -1
        assert fn("z") == 0
        assert fn("aabbc") == 4
    print("모든 테스트 통과")
