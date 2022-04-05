
N = int(input())

def generate_matrix(N):
    A = ['0', '1']
    matrix = A

    for i in range(N - 1):
        new_matrix = []
        for val1 in matrix:
            for val2 in A:
                new_val = val1 + val2
                new_matrix.append(new_val)
        matrix = new_matrix

    return matrix


def generate_matrix_bit_manip(N):
    a = []
    start = 1 << N
    end = 1 << (N + 1)
    for i in range(start, end):
        s = ''
        for j in range(N):
            s += str(i >> j & 1)
        a.append(s)
    return a
