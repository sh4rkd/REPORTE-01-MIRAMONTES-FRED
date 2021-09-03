from lifestore_file import lifestore_accounts
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales


print("Bienvenido al inventario de LifeStore\nPor favor Ingresa tus datos:")

#-----------------Comprobación de usuarios--------------
acceso = True
usuario = -1

while acceso:
  user = input("Usuario: ")
  password = input("Contraseña: ")
  for i in range(0,len(lifestore_accounts)):
    for j in range(0,len(lifestore_accounts)):
      if(lifestore_accounts[i][j+1]==user and lifestore_accounts[i][j+2]==password):
        acceso = False
        usuario = i
        break;
  if(acceso):
    print("No se encontro el usuario.")
  elif(lifestore_accounts[usuario][3]==1):
    print("Accediendo como administrador.")

#------------------En caso de ser administrador----------
salir = True
if(lifestore_accounts[usuario][3]==1):
  while salir:
    print("Bienvenido a la creación de usuarios para administradores, porfavor proporciona los datos del nuevo usuario")
    try:
      user = input("Usuario: ")
      password = input("Contraseña: ")
      lifestore_accounts.append([len(lifestore_accounts),user,password,0])
      print("usuario creado correctamente!, cambiando a la cuenta de",user)
      usuario = len(lifestore_accounts)-1
      salir = False
    except:
      print("Error en la creación de cuenta vuelvalo a intentar")

#-----------Bucle de las opciones------------------
salir = True



while salir:
#------------4 posibles opciones en un print------------
  opcion = input("Bienvenido "+lifestore_accounts[usuario][1]+" Porfavor seleccióne la opción a consultar\n1: Productos más vendidos y productos rezagados\n2: Productos por reseña en el servicio\n3: Total de ingresos y ventas promedio mensuales total anual y meses con más ventas al año\n4: Salir\n")
  try:
#------------si la opcion es 4 sale y da un mensaje------
    if(int(opcion)==4):
      salir = False
      print("Saliendo, gracias por ingresar",lifestore_accounts[usuario][1])

#-----------si la opcion es 1 da otras 2 opciones-------
    elif(int(opcion)==1):
#-----------da otras 2 opciones dependiendo la seleccion
      if(int(input("Productos más vendidos y productos rezagados\nSeleccione \n1: para más vendidos\n2: Para rezagados\n"))==1):
        salir_seleccion_vendidos = True

#----------while para mantenerlos dentro del ciclo de consultar de mayores vendidos.
        while salir_seleccion_vendidos:
          opcion_vendidos = int(input("1: listado de los 50 productos con mayores ventas\n2: uno con los 100 productos con mayor búsquedas\n3: Salir\n"))
          try:
            if(opcion_vendidos == 1):
              for i in lifestore_sales:
                print(i.count(i[1]))
            elif(opcion_vendidos == 2):
              print("pito\n"*2)
            elif(opcion_vendidos == 3):
              salir_seleccion_vendidos = False
              print("Regresando al menu anterior.")
          except:
            print("Error solo numeros")
      else:
        print("puto"*2)  

  except:
    print("Porfavor ingresa solo numeros.")
