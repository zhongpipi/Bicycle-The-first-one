num = [22,333,3,1,11]
list = []

for n in num:
    if len(str(n))%2==0:
        list.append(n)
print(list)
print(len(list))

print(len([i for i in num if len(str(i))%2==0] ))
