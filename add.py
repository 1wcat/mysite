def add(m1, m2):
    m3 = []
    for i in range(len(m1)):
        lst = []
        for j in range(len(m1(i))):
            lst.append(m1[i][j] + m2[i][j])
        m3.append(lst)
    return m3

def test():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[9, 8, 7], [3, 2, 1], [11, 22, 33]]
    mat3 = add(mat1, mat2)
    print(mat3)

test()