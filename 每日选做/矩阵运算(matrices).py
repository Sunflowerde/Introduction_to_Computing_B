def read_matrix():
    row,col=map(int,input().split())
    matrix=[]
    for _ in range(row):
        a=list(map(int,input().split()))
        matrix.append(a)
    return matrix
def matrix_multiplication(A,B):
    if len(A[0])!=len(B):
        return None
    else:
        C=[[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(B[0])):
                    C[i][k]+=A[i][j]*B[j][k]
        return C
def matrix_addition(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        return None
    else:
        C=[[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j]=A[i][j]+B[i][j]
        return C
A=read_matrix()
B=read_matrix()
C=read_matrix()
D=matrix_multiplication(A,B)
if D is None:
    print("Error!")
else:
    E=matrix_addition(D,C)
    if E is None:
        print("Error!")
    else:
        for row in E:
            print(*row)