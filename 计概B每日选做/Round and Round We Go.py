#判断一个数是否为周期数的方法
#若n*(len+1)=9...9(len个9)且n+1为素数时，n为周期数
'''
考虑1/7=0.142857 142857...
当分母为素数时,所得结果为循环小数
以1/7为例,10^6/7=142857.142857...
则(10^6-1)/7=142857,也即142857*(6+1)=999999
'''

def check(s):
    return str(int(s)*(len(s)+1))=="9"*len(s)

while True:
    try:
        s=input()
        if check(s):
            print(f"{s} is cyclic")
        else:
            print(f"{s} is not cyclic")
    except EOFError:
        break