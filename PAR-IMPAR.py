# programa para verificar si un numero es PAR o IMPAR
#input

x = int(input("digite un valor de x:"))

# prosessing
r = (x %2)
if r ==0:
    rta= "PAR"
else:
    rta= "IMPAR"
# output
print("el numero "+ str(x) +"es: "+rta)
