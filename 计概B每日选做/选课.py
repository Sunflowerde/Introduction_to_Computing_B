'''
对一个排列n, 从后向前寻找一个数对(i,i+1), 使a[i]<a[i+1], 这时一定有[i+1,n-1]为降序, 否则假设存在升序，那么在[i+1,n-1]中便能找到升序对, 这与之前寻找的数对矛盾.
这时我们再从后向前遍历, 找到一个j, 使得a[i]<a[j], 此时(i,j)便是最大的较小数与最小的较大数的组合. 将他们两个反转便可得到字典序更大的一组排列.
再对[i+1,n-1]中的数做处理, 由于这个区间内的数一定是降序(这是因为原本较大数存在仍为降序, 后换入一个较小数便也是降序.), 便可使用双指针将这个区间内的数反转, 得到字典序最小的一组, 以此类推, 直到达到要求的重排次数.
'''

def nextpermutation(lst):
    
    length=len(lst)
    i=length-2
    while i>=0 and lst[i]>=lst[i+1]:
        i-=1
    if i>=0:
        j=length-1
        while j>=0 and lst[i]>=lst[j]:
            j-=1
        lst[i],lst[j]=lst[j],lst[i]
        
    left,right=i+1,length-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
        
n=int(input())
m=int(input())
lst=list(map(int,input().split()))

for _ in range(m):
    nextpermutation(lst)
    
print(*lst)