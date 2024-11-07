def read_matrix(n,m):
    matrix=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix
n,m=map(int,input().split())
matrix=read_matrix(n,m)
result=[]
for i in range(n):
    for j in range(m):
        ABCD=matrix[0][j]*1000+matrix[i][-1]*100+matrix[-1][j]*10+matrix[i][0]
        result.append(matrix[i][j]*ABCD)
print(max(result))