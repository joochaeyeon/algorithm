# 시간복잡도 제한 X -> 완전탐색 방법 이용!
# 엄청 어려운 문제...!!
# ⭐⭐⭐⭐⭐

def rotate_90(matrix):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]  # n*n 새로운 배열 생성

    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j] 
    return new_matrix 

# 자물쇠(lock)의 모든 홈(0)이 채워져 1이 되었는지 확인하는 함수!
def check(new_lock, lock_size):
    for i in range(lock_size):
        for j in range(lock_size):
            if new_lock[lock_size + i][lock_size + j] != 1:
                return False
    return True

def solution(key, lock):
    n, m = len(lock), len(key)
    new_size = n + 2 * m #90도 회전 및 움직이면서 확인해야하기에 더 큰 사이즈로 초기화 시켜줌!
    new_lock = [[0] * new_size for _ in range(new_size)]
    
    for i in range(n):
        for j in range(n):
            new_lock[m + i][m + j] = lock[i][j]
    
    for rotation in range(4): #90씩 4번 회전 가능
        key = rotate_90(key)
        for x in range(n + m): #key를 new_lock의 모든 위치에 이동시키면서 검사 -> n+m
            for y in range(n + m):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if check(new_lock, n):
                    return True
                
                for i in range(m): # 제자리에 돌려놓고 90도 회전시켜 위치 이동시킴!
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False


# 0:홈, 1:돌기
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))