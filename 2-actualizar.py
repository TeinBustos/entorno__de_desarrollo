import psycopg2



#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='12345678',  
                          host='localhost',
                          port='5432',
                          database='python')

# utilizar cursor
cursor=conexion.cursor()

# crear sentencia sql
sql='UPDATE personas SET nombre=%s,apellido=%s,edad=%s WHERE persona_id=%s'

# consulta de datos a usuario
persona_id=input('ingrese id de la persona a editar: ')
nombre=input('ingrese nombre: ')
apellido=input('ingrese apellido: ')
edad=input('ingrese edad: ')

#recoleccion de datos
datos=(nombre,apellido,edad,persona_id)

# utilizar el metodo execute
cursor.execute(sql,datos)

# guardar modificacion
conexion.commit()

#contar el numero de cambios
actualizacion=cursor.rowcount

# mostrar mensaje al usuraio
print(f'registro actualizado: {actualizacion}')

# cerrar conexiones
cursor.close()
conexion.close()