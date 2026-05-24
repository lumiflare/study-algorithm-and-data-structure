# Python 코딩테스트 필수 패턴

## 1. 빠른 입출력

```python
import sys
input = sys.stdin.readline

# 정수 하나
n = int(input())

# 한 줄에 여러 정수
a, b, c = map(int, input().split())

# 리스트 입력
arr = list(map(int, input().split()))

# 여러 줄 입력
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 빠른 출력 (많은 출력 시)
sys.stdout.write(str(result) + '\n')
```

## 2. collections 모듈

```python
from collections import Counter, defaultdict, deque

# Counter — 빈도수 세기
freq = Counter([1, 2, 2, 3, 3, 3])  # {3: 3, 2: 2, 1: 1}
freq.most_common(2)  # [(3, 3), (2, 2)]

# defaultdict — 기본값 딕셔너리
graph = defaultdict(list)
graph[1].append(2)  # KeyError 없이 자동 생성

# deque — 양방향 큐 (BFS 필수)
q = deque([1, 2, 3])
q.appendleft(0)  # O(1) 왼쪽 삽입
q.popleft()      # O(1) 왼쪽 제거
```

## 3. heapq — 힙 (우선순위 큐)

```python
import heapq

# 최소힙
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
min_val = heapq.heappop(heap)  # 1

# 최대힙 (부호 반전 트릭)
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# 리스트를 힙으로 변환
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)  # O(N)

# Top K (K개의 가장 큰/작은 원소)
heapq.nlargest(k, arr)
heapq.nsmallest(k, arr)
```

## 4. itertools — 순열, 조합, 곱

```python
from itertools import permutations, combinations, product, combinations_with_replacement

# 순열 (nPr)
list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 조합 (nCr)
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]

# 중복 조합
list(combinations_with_replacement([1,2,3], 2))

# 데카르트 곱 (중첩 루프 대체)
list(product([0,1], repeat=3))  # 000, 001, 010, ..., 111
```

## 5. bisect — 이진 탐색

```python
from bisect import bisect_left, bisect_right, insort

arr = [1, 3, 5, 7, 9]

# lower bound (val 이상인 첫 인덱스)
idx = bisect_left(arr, 5)   # 2

# upper bound (val 초과인 첫 인덱스)
idx = bisect_right(arr, 5)  # 3

# 정렬 유지하며 삽입
insort(arr, 4)  # [1, 3, 4, 5, 7, 9]

# 범위 내 개수: [lo, hi) 구간의 원소 수
count = bisect_right(arr, hi) - bisect_left(arr, lo)
```

## 6. 방향 벡터 (2D 격자)

```python
# 4방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 8방향 (대각선 포함)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 범위 체크
def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 이동
for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny, n, m) and not visited[nx][ny]:
        visited[nx][ny] = True
        # 처리
```

## 7. BFS 템플릿

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## 8. DFS 템플릿

```python
# 재귀 DFS
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 스택 DFS
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
```

## 9. 재귀 제한 해제

```python
import sys
sys.setrecursionlimit(10**6)  # 기본값 1000 → 100만으로
```

## 10. 무한대

```python
INF = float('inf')
# 또는
INF = int(1e9)
```

## 11. 정렬 팁

```python
# key 함수로 정렬 기준 지정
arr.sort(key=lambda x: x[1])           # 두 번째 원소 기준
arr.sort(key=lambda x: (-x[0], x[1]))  # 첫째 내림차순, 둘째 오름차순

# 튜플 정렬 (자동 사전순)
points = [(3, 1), (1, 2), (1, 1)]
points.sort()  # [(1, 1), (1, 2), (3, 1)]
```

## 12. 자주 쓰는 수학

```python
import math

math.gcd(a, b)       # 최대공약수
math.lcm(a, b)       # 최소공배수 (Python 3.9+)
math.comb(n, r)       # 조합 nCr (Python 3.8+)
math.isqrt(n)         # 정수 제곱근

# 에라토스테네스의 체
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime
```
