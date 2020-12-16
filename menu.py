import sqlite3

# Para conectarnos a la BD
def validar():
    usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese clave de usuario: ")
    if usuario == "Sergio Vite" and clave == 'SEVI':
            menuPrincipal()
    elif usuario == 'Javier Quispe' and clave == 'JAQU':
            menuPrincipal()
    elif usuario == 'jamil zalsar' and clave == 'PARA':
            menuPrincipal()
    elif usuario == 'jorge galiar' and clave == 'BRCO':
            menuPrincipal()
    elif usuario == 'Mario Quispe' and clave == 'JASA':
            menuPrincipal()
    else:
        print("Usuario o clave incorrecta")
        
    
def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("===== DATOS PRODUCTO =====")
            print("1. Listar")
            print("2. Agregar")
            print("3. Eliminar")
            print("4. Modificar")
            print("5. Salir")
            opcion = int(input("Seleccione una opccion: "))
        
            if opcion < 1 or opcion > 5:
                print("Opccion invalida, INGRESE NUEVAMENTE")
                
            else:
                if opcion == 5:
                    print("Gracias por usar este sistema")
                    continuar=False
                    break
                else:
                    opcionCorrecta=True
                    ejecutarOpcion(opcion)
            
def ejecutarOpcion(opcion):

        if opcion == 1:
            print("1. lISTAR PRODUCTOS")
            import sqlite3
            conexion = sqlite3.connect("ventas.db")
            cursor = conexion.cursor()
            cursor.execute(""" SELECT *
                                   FROM PRODUCTO
                                   ORDER BY NOMBRE
                               """)
                # Todo el resultado del select está en Personas
                # en java lo conocemos como el ResultSet
            producto = cursor.fetchall()
        
            for producto in producto:
                print(producto)
                    
                # Cerrar Conexión
                conexion.close() 

        elif opcion == 2:
            print(" Agregar Producto")
            import sqlite3
            conexion = sqlite3.connect("ventas.db")
            cursor = conexion.cursor()
                
            p = input("Ingrese producto: ")
            e = input("Ingrese codigo: ")
            f = input("Ingrese precio: ")
            cursor.execute('INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO) VALUES(?,?,?)',(p,e,f))
            
            conexion.commit()
            conexion.close()
        elif opcion == 3:
            import sqlite3
            conexion = sqlite3.connect("ventas.db")
            cursor = conexion.cursor()
            n = int(input("ID del elemento a cambiar: "))
            p = input("Nuevo nombre del elemento a cambiar: ")
            e = input("Nuevo estado del elemento a cambiar: ")
            
            
            cursor.execute("UPDATE PAIS SET NOMBRE = '%s', ESTADO = '%s' WHERE IDPAIS = '%s'" %(p,e,n))
            conexion.commit()
            conexion.close()
        elif opcion == 4:
            print("HOLA")
        else:
            print("HOLA")
        
validar()
menuPrincipal()