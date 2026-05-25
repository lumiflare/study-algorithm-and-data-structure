"""
문제: 최빈 문자 (동점 시 알파벳 순)
출처: 자체 출제
난이도: Easy
카테고리: 배열 & 해싱
핵심 패턴: Counter + 동점 처리 (사전 정렬 트릭 / 명시적 key 함수)
시간 복잡도: O(N log N) 또는 O(N + U log U)
공간 복잡도: O(N)
"""

from collections import Counter


# 스타일 A: 사전 정렬 트릭
# Counter의 삽입 순서 = 정렬된 알파벳 순 → most_common이 동점을 알파벳 순으로 처리
def most_frequent_char_a(s: str) -> tuple[str, int]:
    return Counter(sorted(s)).most_common(1)[0]


# 스타일 B: 명시적 key 함수 (가장 명확)
# (-빈도, 문자) 튜플 비교: 빈도 큰 순, 동률은 문자 사전순
def most_frequent_char_b(s: str) -> tuple[str, int]:
    freq = Counter(s)
    ch = min(freq, key=lambda c: (-freq[c], c))
    return (ch, freq[ch])


# 스타일 C: 배열 카운트 (소문자 알파벳 한정 — 가장 빠름)
def most_frequent_char_c(s: str) -> tuple[str, int]:
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1
    best_idx = 0
    for i in range(26):
        if cnt[i] > cnt[best_idx]:
            best_idx = i
    return (chr(best_idx + ord('a')), cnt[best_idx])


if __name__ == "__main__":
    for fn in (most_frequent_char_a, most_frequent_char_b, most_frequent_char_c):
        assert fn("programming") == ('g', 2), fn("programming")
        assert fn("abc") == ('a', 1)
        assert fn("aabbcc") == ('a', 2)
        assert fn("zzz") == ('z', 3)
        assert fn("a") == ('a', 1)
    print("모든 테스트 통과")
