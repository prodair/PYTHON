#Triangulo
a=int(input("Lado 1:"))
b=int(input("Lado 2:"))
c=int(input("Lado 3:"))

#Verifica se forma triangulo
if (b+c)>a and (a+c)>b and (a+b)>c:
  if a==b and a==c:
    print("Triângulo equilátero.")
  elif a==b or a==c or b==c:
    print("Triângulo isósceles.")
  else:
    print("Triângulo escaleno.")
else:
  print("As medidas informadas não formam um triângulo.")