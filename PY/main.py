from lifestore_file import lifestore_accounts

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
  else:
    print("Accediendo como usuario.")


