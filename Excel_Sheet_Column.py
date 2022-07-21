n=int(input())
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st='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 '
while n:
    i=n%26
    if i==0:
        st+='Z'
        n=(n//26)-1
    else:
        st+=s[i-1]
        n=(n//26)
l=len(st)
for i in range(l-1,-1,-1):
    print(st[i],end='')