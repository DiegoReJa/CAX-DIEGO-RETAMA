nombre=input("Nombre del cajero: ")
print('Bienvenido a Tienda Doña pelos')

producto1=input('primer producto: ')

producto2=input('segundo producto: ')

producto3=input('tercer producto: ')

producto4=input('cuarto producto: ')

producto5=input('quinto producto: ')

subtotal1=int(input('precio del primer producto:  '))       
subtotal2=int(input('precio del segundo producto: ')) 
subtotal3=int(input('precio del tercer producto: '))
subtotal4=int(input('precio del cuarto producto: '))
subtotal5=int(input('precio del quinto producto: '))


print("TICKER")

print("1. ", producto1,"$",subtotal1)
print("2. ",producto2,"$",subtotal2)
print("3. ",producto3,"$",subtotal3)
print("4. ",producto4,"$",subtotal4)
print("5. ",producto5,"$",subtotal5)
subtotal=subtotal1+subtotal2+subtotal3+subtotal4+subtotal5
print('el subtotal es: ',subtotal)

IVA=subtotal*.16

print('el IVA es: ',IVA)

total=subtotal+IVA

print('el total de la compra es: ',total)

pago=input('Metodo de pago: ')
print(pago)
Ticket=input('Muchas gracias por su compra, vuelva pronto')