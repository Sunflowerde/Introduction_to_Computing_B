dic1={0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
          10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
          100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
          1000:"M"}
dic2={value:key for key,value in dic1.items()}
def change1(n):
    n=int(n)
    a1=n//1000
    a2=(n%1000)//100
    a3=(n%100)//10
    a4=n%10
    return a1*"M"+dic1[a2*100]+dic1[a3*10]+dic1[a4]
def change2(s):
    total=0
    last_value=0
    for char in reversed(s):
        if dic2[char]<last_value:
            total-=dic2[char]
        else:
            total+=dic2[char]
        last_value=dic2[char]
    return total
s=input()
if s.isdigit():
    print(change1(s))
else:
    print(change2(s))