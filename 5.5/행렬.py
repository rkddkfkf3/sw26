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
# 행렬 출력 (예쁘게)
def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:5}", end=" ")
        print()
    print()
# A x B + C 계산
def matrix_calculate(A, B, C):
    n = len(A)
    # A x B 저장할 행렬
    AB = []
    for i in range(n):
        row = []
        for j in range(n):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            row.append(total)
        AB.append(row)
    # (A x B) + C 계산
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(AB[i][j] + C[i][j])
        result.append(row)
    return result
# 출력
n = int(input("1보다 크고 5보다 작거나 같은 N 입력: "))
if 1 < n <= 5:
    A = make_matrix(n)
    B = make_matrix(n)
    C = make_matrix(n)

    print("[A 행렬]")
    print_matrix(A)

    print("[B 행렬]")
    print_matrix(B)

    print("[C 행렬]")
    print_matrix(C)

    result = matrix_calculate(A, B, C)

    print("[A x B + C 결과]")
    print_matrix(result)

else:
    print("Input Error")