#Triangulo
a=int(input("Lado 1:"))
b=int(input("Lado 2:"))
c=int(input("Lado 3:"))

#Verifica se forma triangulo
if (b+c)>a and (a+c)>b and (a+b)>c:
  if a==b and a==c:
    print("Tri�ngulo equil�tero.")
  elif a==b or a==c or b==c:
    print("Tri�ngulo is�sceles.")
  else:
    print("Tri�ngulo escaleno.")
else:
  print("As medidas informadas n�o formam um tri�ngulo.")