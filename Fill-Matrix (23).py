def fill_mat(x,y):
    matrix = [[0 for _ in range(x)] for _ in range(y)]
    num = 1
    for i in range(y):
        if i%2==0:
            for j in range(x):
                matrix[i][j] = num
                num += 1
        else:
            for l in range(x-1,-1,-1):
                matrix[i][l] = num
                num += 1
    return matrix

def print_mat(mat):
    for i in mat:
        print(i)

print_mat(fill_mat(4,5))