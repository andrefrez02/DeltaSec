n1=int(input("O seu numero é "))


print("[2] Binario")
print("[3] Hexadecimal")
print("[4] octadecimal")

if n1 < 0:
    print("Invalido")
    

op=int(input("Você quer tranformar ele em "))
print("Numero invalido")
print("[2] Binario")
print("[3] Hexadecimal")
print("[4] octadecimal")

c=int(input("Você quer tranformar ele em "))

if c==1:
    b=bin(n1)
    print("Para binario" , b )
elif c==2:
    h=hex(n1)
    print("Para hex" , h)

else:
    o=oct(n1)
    print("Para oct" , o)
    


