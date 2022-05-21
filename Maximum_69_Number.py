def maximum69number(self,num:int)->int:
    return(str(num).replace('6','9',1))
n=input()
print(maximum69number(1,n))