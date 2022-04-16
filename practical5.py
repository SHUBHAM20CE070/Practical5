#20CE070_Shubham Panchal
#prac5
#Swap Case

a = input()
str = ''
for i in a:
    if i == i.upper():
        str+=i.lower()
    elif i == i.lower():
        str+=i.upper()
    else:
        str+=i
print(str)
