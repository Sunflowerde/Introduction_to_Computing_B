n=int(input())
haab_dic={"pop":0,"no":1,"zip":2,"zotz":3,"tzec":4,"xul":5,"yoxkin":6,"mol":7,"chen":8,"yax":9,"zac":10,"ceh":11,"mac":12,"kankin":13,"muan":14,"pax":15,"koyab":16,"cumhu":17,"uayet":18}
tzolkin_dic={0:"imix",1:"ik",2:"akbal",3:"kan",4:"chicchan",5:"cimi",6:"manik",7:"lamat",8:"muluk",9:"ok",10:"chuen",11:"eb",12:"ben",13:"ix",14:"mem",15:"cib",16:"caban",17:"eznab",18:"canac",19:"ahau"}

print(n)

for _ in range(n):
    day,month,year=input().split()
    day=int(day.rstrip("."))
    total=day+haab_dic[month]*20+int(year)*365
    print(total%13+1,tzolkin_dic[total%20],total//260)