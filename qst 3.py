# str=input("enter a string:")
vowels=["a","e","i","o","u"]
str=[8,"a",0,"h","a","i",8,"g","l"]
result=[]
for i in str:
    if i not in vowels and type(i) !=int:
        result.append(i)
print(result)


  