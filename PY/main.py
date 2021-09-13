from lifestore_file import lifestore_accounts
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches
import pandas as pd
import numpy as np

df_ventas = pd.DataFrame(lifestore_sales, columns=['id_sale','id_product', 'score' , 'date','refund' ])

df_productos = pd.DataFrame(lifestore_products, columns=['id_product', 'name', 'price', 'category', 'stock'])
    
df_busqueda = pd.DataFrame(lifestore_searches, columns = ['id_search', 'id_product'])

print("Bienvenido al inventario de LifeStore\nPor favor ingresa tus datos:")

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
    print("Bienvenido a la creación de usuarios para administradores, por favor proporciona los datos del nuevo usuario.")
    try:
      user = input("Usuario: ")
      password = input("Contraseña: ")
      lifestore_accounts.append([len(lifestore_accounts),user,password,0])
      print("¡Usuario creado correctamente!, cambiando a la cuenta de "+user+".")
      usuario = len(lifestore_accounts)-1
      salir = False
    except:
      print("Error en la creación de cuenta vuelvalo a intentar")

#-----------Bucle de las opciones------------------
salir = True



while salir:
  try:
    #------------4 posibles opciones en un print------------
    opcion = input("Bienvenido, "+lifestore_accounts[usuario][1]+". Por favor seleccione la opción a consultar:\n1: productos más vendidos y productos rezagados,\n2: productos por reseña en el servicio,\n3: total de ingresos mensual, ventas promedio mensual, total de ventas anual y meses con más ventas al año,\n4: salir.\n")
#------------si la opcion es 4 sale y da un mensaje------
    if(int(opcion)==4):
      salir = False
      print("Saliendo, gracias por ingresar",lifestore_accounts[usuario][1])

#-----------si la opcion es 1 da otras 2 opciones-------
    elif(int(opcion)==1):
      salir_seleccion_vendidos_rezagados = True      
      while(salir_seleccion_vendidos_rezagados):
        try:  
          opcion_vendidos_rezagados = int(input("Productos más vendidos y productos rezagados\nSeleccione \n1: para más vendidos,\n2: Para rezagados,\n3: Para salir.\n"))
          if(opcion_vendidos_rezagados==1):
            salir_seleccion_vendidos = True

  #----------while para mantenerlos dentro del ciclo de consultar de mayores vendidos.
              
            while salir_seleccion_vendidos:
              try:
                opcion_vendidos = int(input("1: listado de los 50 productos con mayores ventas,\n2: uno con los 100 productos con mayor búsquedas,\n3: Salir.\n"))
  #en caso de la opción 1 generar una lista de hasta 50 productos que sean los que tienen mayores ventas
                if(opcion_vendidos == 1):
                  top_ventas = pd.DataFrame(df_ventas.groupby('id_product').size().nlargest(50))
                  top_ventas = pd.merge(top_ventas, df_productos, on='id_product')
                  top_ventas = top_ventas.rename(columns={0:'total_ventas'})              
                  top_ventas = top_ventas.rename(columns={"name":'nombre_producto'})
                  print(top_ventas.iloc[:,[1,2]])
  #en caso de la opción 2 generar una lista con los hasta 100 productos mas buscados
                elif(opcion_vendidos == 2):
                  top_busqueda = pd.DataFrame(df_busqueda.groupby('id_product').size().nlargest(100))
                  top_busqueda = pd.merge(top_busqueda, df_productos, on='id_product')
                  top_busqueda = top_busqueda.rename(columns={0:'total_busquedas'})              
                  top_busqueda = top_busqueda.rename(columns={"name":'nombre_producto'})
                  print(top_busqueda.iloc[:,[1,2]])
  #en caso 3 regresar al menu anterior para seguir con el programa.
                elif(opcion_vendidos == 3):
                  salir_seleccion_vendidos = False
                  print("----------------------------------------------------\nRegresando al menu anterior.\n")
                else:
                  print("Selecciona una opción del 1 al 3.")
              except:
                print("----------------------------------------------------\nError solo numeros\n")
          elif(opcion_vendidos_rezagados == 2):
            salir_seleccion_rezagados = True
            while salir_seleccion_rezagados:
              try:
                opcion_no_vendidos = int(input("1: listado de los 50 productos con menores ventas,\n2: uno con los 100 productos con menores búsquedas,\n3: Salir.\n"))
                if(opcion_no_vendidos == 1):
                  peores_ventas = pd.DataFrame(df_ventas.groupby('id_product').size().nsmallest(50))
                  peores_ventas = pd.merge(peores_ventas, df_productos, on='id_product')
                  peores_ventas = peores_ventas.rename(columns={0:'total_ventas'})              
                  peores_ventas = peores_ventas.rename(columns={"name":'nombre_producto'})
                  print(peores_ventas.iloc[:,[1,2]])
  #en caso de la opción 2 generar una lista con los hasta 100 productos mas buscados
                elif(opcion_no_vendidos == 2):
                  peores_busqueda = pd.DataFrame(df_busqueda.groupby('id_product').size().nsmallest(100))
                  peores_busqueda = pd.merge(peores_busqueda, df_productos, on='id_product')
                  peores_busqueda = peores_busqueda.rename(columns={0:'total_busquedas'})              
                  peores_busqueda = peores_busqueda.rename(columns={"name":'nombre_producto'})
                  print(peores_busqueda.iloc[:,[1,2]])
  #en caso 3 regresar al menu anterior para seguir con el programa.
                elif(opcion_no_vendidos == 3):
                  salir_seleccion_rezagados = False
                  print("----------------------------------------------------\nRegresando al menu anterior.\n")
                else:
                  print("Selecciona una opción del 1 al 3.")
              except:
                print("----------------------------------------------------\nError solo numeros\n")
          elif(opcion_vendidos_rezagados == 3):
            salir_seleccion_vendidos_rezagados = False
            print("----------------------------------------------------\nRegresando al menu anterior.\n")
        except Exception as e:
          print(e)

#opción 2 del menu principal ------------------------------------  
    elif(int(opcion)==2):
      salir_seleccion_resenia = True
      resenias = df_ventas.groupby('id_product').agg({'score':min,'refund':np.sum})\
        .rename(columns={'score':'min_score'},inplace=False)            
      resenias = resenias.sort_values(by='min_score',ascending=False)
      while(salir_seleccion_resenia):
        try:
          opcion_resenia = int(input("1: Mejores reseñas,\n2: peores Reseñas,\n3: Salir.\n"))
          if(opcion_resenia == 1):
             mejores_resenias = resenias.nlargest(20,columns='min_score')
             mejores_resenias = pd.merge(mejores_resenias, df_productos, on='id_product')             
             mejores_resenias = mejores_resenias.rename(columns={"name":'nombre_producto'})          
             mejores_resenias = mejores_resenias.rename(columns={"min_score":'puntos_reseña'})          
             mejores_resenias = mejores_resenias.rename(columns={"refund":'reembolso'})


             print(mejores_resenias.iloc[:,[3,1,2]])

          elif(opcion_resenia == 2):
             peores_resenias = resenias.nsmallest(20,columns='min_score')
             peores_resenias = pd.merge(peores_resenias, df_productos, on='id_product')
             print(peores_resenias.iloc[:,[3,1,2]])

          elif(opcion_resenia == 3):
            salir_seleccion_resenia = False
            print("----------------------------------------------------\nRegresando al menu anterior.\n")
          else:
            print("Opciones del 1 al 3")

        except:
          print("Error solo numeros.")
    
    elif(int(opcion)==3):
      df_ventas = df_ventas[df_ventas['refund'] == 0]
      salir_seleccion_total_ingresos = True
      while(salir_seleccion_total_ingresos):
        opcion_total_ingresos = int(input("1: total de ingresos mensual,\n2: ventas promedio mensual,\n3: total de ventas anual,\n4: meses con más ventas al año,\n5: salir.\n"))

        if(opcion_total_ingresos == 1):
          ventas_mensuales = df_ventas.join(df_productos.set_index('id_product'), on='id_product')
          ventas_mensuales = ventas_mensuales[['date','price']]
          ventas_mensuales['date'] = pd.to_datetime(ventas_mensuales['date'])
          ventas_mensuales = ventas_mensuales.groupby(ventas_mensuales['date'].dt.strftime('%m')).agg({'price':np.sum})
          pd.DataFrame(ventas_mensuales)
          print(ventas_mensuales,"\n")

        elif(opcion_total_ingresos == 2):
          promedio_mensuales = df_ventas.join(df_productos.set_index('id_product'), on='id_product')
          promedio_mensuales = promedio_mensuales[['date','price']]
          promedio_mensuales['date'] = pd.to_datetime(promedio_mensuales['date'])
          promedio_mensuales = promedio_mensuales.groupby(promedio_mensuales['date'].dt.strftime('%m')).agg({'price':np.mean})          
          print(promedio_mensuales,"\n")

        elif(opcion_total_ingresos == 3):
          promedio_mensuales = df_ventas.join(df_productos.set_index('id_product'), on='id_product')
          promedio_mensuales = promedio_mensuales[['date','price']]
          promedio_mensuales['date'] = pd.to_datetime(promedio_mensuales['date'])
          promedio_mensuales = promedio_mensuales.groupby(promedio_mensuales['date'].dt.strftime('%m')).agg({'price':np.sum})
          total_anual = round(np.sum(promedio_mensuales['price']),2)
          print("El total anual es de $",total_anual,"\n")
        
        elif(opcion_total_ingresos == 4):
          ventas_mensuales = df_ventas.join(df_productos.set_index('id_product'), on='id_product')          
          ventas_mensuales['date'] = pd.to_datetime(ventas_mensuales['date'])
          top_monthly_sales = ventas_mensuales.groupby(ventas_mensuales['date'].dt.strftime('%m')).agg({'price':np.sum}).nlargest(12,columns='price')
          top_monthly_sales.rename(columns={'price':'sales'})
          top_monthly_sales.columns=['sale_sum']
          print(top_monthly_sales,"\n")

        elif(opcion_total_ingresos == 5):
            salir_seleccion_total_ingresos = False
            print("----------------------------------------------------\nRegresando al menu anterior.\n")
        
        else:
          print("Opciones del 1 al 5")

        


      
  except Exception as e:
    print(e)
