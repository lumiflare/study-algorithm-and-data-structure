"""
문제: Valid Anagram — 두 문자열이 같은 문자 구성(아나그램)인가
출처: LeetCode 242
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: 빈도수 비교 (Counter 동등성) 또는 정렬 비교 + 길이 조기 종료
시간 복잡도: O(N) (Counter) / O(N log N) (정렬)
공간 복잡도: O(1) (알파벳 한정 Counter) / O(N) (정렬)
"""

from collections import Counter


# A) 정렬 비교 — 가장 짧고 직관적
def is_anagram_sort(s: str, t: str) -> bool:
    # 길이 다르면 정렬해도 다름 — 조기 종료로 빠르게 False
    if len(s) != len(t):
        return False
    # sorted()는 문자열을 받아 정렬된 리스트 반환 — list() 변환 불필요
    return sorted(s) == sorted(t)


# B) Counter 비교 — Pythonic, 길이가 클수록 유리
def is_anagram_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # 두 Counter는 모든 (키, 값) 쌍이 같을 때만 ==
    return Counter(s) == Counter(t)


# C) 알파벳 한정 미세 최적화 — 26 배열에 +1/-1
def is_anagram_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for cs, ct in zip(s, t):
        count[ord(cs) - ord('a')] += 1
        count[ord(ct) - ord('a')] -= 1
    return all(c == 0 for c in count)


if __name__ == "__main__":
    for fn in (is_anagram_sort, is_anagram_counter, is_anagram_array):
        assert fn("anagram", "nagaram") is True
        assert fn("rat", "car") is False
        assert fn("a", "ab") is False
        assert fn("aacc", "ccac") is False
        assert fn("", "") is True
        assert fn("ab", "ba") is True
    print("모든 테스트 통과")
