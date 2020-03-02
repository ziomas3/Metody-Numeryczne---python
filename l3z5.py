import numpy as np
import scipy as sc
def gauss(A,b):
  n = len(A)
  M = A
  
  i = 0
  for x in M:
   x.append(b[i]) #b wyrazy wolne
   i += 1
 #eliminacja
  for k in range(n): #sortowanie
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k] #zamiana wierszy
     

   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k] #mnoznik
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m] #odejmowanie linii

  x = [0 for i in range(n)] #zerowanie x

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  return(x)

A4= [[1,0,0,0,0],[1,1,1,1,1],[1,3,9,27,81],[1,5,25,125,625],[1,6,36,216,1296]]
b4= [-1,1,3,2,-2]
print(gauss(A4,b4))

A3=[[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]]
b3=[1,1,-4,-2,-1]
print(gauss(A3,b3))

A1=[[-1,1,-4],[2,2,0],[3,3,2]]
b1=[0,1,0.5]
print(gauss(A1,b1))

L=[[1,0,0],[3/2,1,0],[1/2,11/13,1]]
U=[[2,-3,-1],[0,13/2,-7/2],[0,0,32/13]]
b2=[1,-1,2]
y=gauss(L,b2)
print(y)
print(gauss(U,y))


