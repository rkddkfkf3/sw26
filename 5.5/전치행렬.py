import random
# 랜덤 행렬 
def make_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = random.randint(1, n * n * 10 - 1)
            row.append(value)
        matrix.append(row)
    return matrix
# 행렬 출력 (예쁘게,,)
def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:5}", end=" ")
        print()
    print()
# 전치행렬 함수
def transpose_matrix(matrix):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result
# 출력
n = int(input("1보다 크고 5보다 작거나 같은 N 입력: "))
if 1 < n <= 5:
    A = make_matrix(n)
    print("[원래 행렬]")
    print_matrix(A)

    T = transpose_matrix(A)
    print("[전치 행렬]")
    print_matrix(T)

else:
    print("Input Error")