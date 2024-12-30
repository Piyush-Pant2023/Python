s=input("Enter the string: ")
u,l,d=0,0,0
word=1
print(len(s))
for i in range(len(s)):
    if s[i].isupper():
        u+=1
    elif s[i].islower():
        l+=1
    elif s[i].isdigit():
        d+=1
    elif s[i].isspace() and s[i+1].isalnum():
        word+=1
print(u,l,d,word)