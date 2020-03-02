import math
for n in range(2, 250, 2):
    x=pow(2,-n)
    print(n,"\t", math.sqrt(pow(x,2)+1)-1,"\t",x**2/(math.sqrt(pow(x,2)+1)+1))