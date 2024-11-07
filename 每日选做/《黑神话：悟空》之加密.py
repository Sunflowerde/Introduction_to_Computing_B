k=int(input())
s=input()
string=""
for char in s:
    if ord("a")<=ord(char)<=ord("z"):
        string+=chr(ord("a")+(ord(char)-ord("a")-k)%26)
    if ord("A")<=ord(char)<=ord("Z"):
        string+=chr(ord("A")+(ord(char)-ord("A")-k)%26)
print(string)