n: str = input().lower()
s: str = input()

p: list[str] = s.split("/")

print(("Bukan yang ini. SKIP!","Nah, ini dia!")[sum(map(n.__contains__,("bun","ny","hop")))>0 and 10<len(s)<25 and not sum(map(lambda x:not x.isalnum(),"".join(p))) and [*map(len,p)]==[*range(2,len(p)+2)]])
