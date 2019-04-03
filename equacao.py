import math
#Equação segundo grau
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if a!=0:
  delta=b*b-4*a*c
  print("Delta=",delta)
  if delta==0:
    print("Raiz da equação:", (-b+math.sqrt(delta))/2*a)
  elif delta>0:
    print("Raiz 1 da equação :", (-b+math.sqrt(delta))/2*a)
    print("Raiz 2 da equação :", (-b-math.sqrt(delta))/2*a)
  else:
    print("Não existem raízes reais")
  
else:
  print("Se a=0 então não é equação do segundo grau.")