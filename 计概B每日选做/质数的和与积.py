s=int(input())
def prime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
for i in range(s//2,1,-1):
    if prime(i):
        if prime(s-i):
            print(i*(s-i))
            break