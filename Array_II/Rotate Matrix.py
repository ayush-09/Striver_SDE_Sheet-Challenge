mat = [[1,2,3],[4,5,6],[7,8,9]]
# matrix.reverse()
# print(matrix)

def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix

if __name__=="__main__":
    print(rotate(matrix=mat))