import math
#Equa��o segundo grau
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if a!=0:
  delta=b*b-4*a*c
  print("Delta=",delta)
  if delta==0:
    print("Raiz da equa��o:", (-b+math.sqrt(delta))/2*a)
  elif delta>0:
    print("Raiz 1 da equa��o :", (-b+math.sqrt(delta))/2*a)
    print("Raiz 2 da equa��o :", (-b-math.sqrt(delta))/2*a)
  else:
    print("N�o existem ra�zes reais")
  
else:
  print("Se a=0 ent�o n�o � equa��o do segundo grau.")