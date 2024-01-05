import re
#копируем элемент с тега ul
f = open('список.txt', 'r', encoding='utf-8').read()

# r = re.findall(r'[А-Я][а-я]+ [А-Я][а-я]+', f)
r = re.findall(r'class="Link"><span>\w+ \w+', f)  #с беседы вк
#r = re.findall(r'<div class="fans_fan_name">\w+', f)
t = 0

for i in range(len(r)):
    t += 1
    r[i] = r[i].replace('class="Link"><span>', '') #с беседы в вк

for i in r: print(i)
# print(r)

with open('опрос.txt', encoding="utf-8") as v:
    k=1
    n=0
    m=[]
    for line in v:
        n+=1
        if n == k:
            m.append(line)
            k+=3

print(m)