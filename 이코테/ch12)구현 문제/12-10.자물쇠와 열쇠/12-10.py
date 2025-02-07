# ⭐⭐⭐⭐
# 어려운 문제
# 문제를 읽고 필요한 함수가 총 몇개인지 파악하고 코드 구현하기❗

# 90도 회전시키기
def rotate_90(matrix): #matrix n*n 배열이 들어옴
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]  # n*n 새로운 배열 생성

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]  # 90도 회전

    return rotated 


# 확장된 lock에서 자물쇠 부분이 모두 1인지 확인하는 함수
def check(new_lock, lock_size, key_size):
    for i in range(lock_size):
        for j in range(lock_size):
            if new_lock[key_size - 1 + i][key_size - 1 + j] != 1: 
                return False
    #new_lock의 해당 영역이 모두 1이어야만 True 반환
    return True 


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)

    #key가 움직일 수 있는 확장된 lock부분 만들기
    new_size = lock_size + (key_size - 1) * 2
    new_lock = [[0] * new_size for _ in range(new_size)]

    #확장된 matrix 가운데에 원래 lock값 넣기
    for i in range(lock_size):
        for j in range(lock_size):
            new_lock[key_size - 1 + i][key_size - 1 + j] = lock[i][j]

    for _ in range(4):  # 0,90,180,270 -> 4번 회전 가능
        key = rotate_90(key) 

        for x in range(new_size - key_size + 1):
            for y in range(new_size - key_size + 1):
                # 열쇠 끼우기
                for i in range(key_size):
                    for j in range(key_size):
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 검사 로직 적용
                if check(new_lock, lock_size, key_size):
                    return True

                # 원상복구
                for i in range(key_size):
                    for j in range(key_size):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


# 테스트
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))  
