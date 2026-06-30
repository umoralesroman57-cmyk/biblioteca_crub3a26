from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_libros():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in libros:
                print("------------------------------")
                print(
                    f"ID: {libro.id}, Titulo {libro.titulo},"
                    f"Autor: {libro.autor}, ISBN: {libro.isbn},"
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("--------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    titulo = input("Escribe el titulo del nuevo libro: ")
    autor = input("Escribe el id del autor: ")
    isbn = input("Escriba el isbn del nuevo libro: ")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercción realizada con exito")
    except Exception as e:
        print("Errror al insertar un nuevo libro")
        print(e)

def actualizar_libro():
    print("Seleciona el libro a actualizar")
    try:
        libro_dao= LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar"))
        titulo = input("Escribe el nuevo titulo")
        autor = input("Escribe el nuevo autor")
        isbn = input("Escribe el nuevo ISBN")
        disponible = bool(input("Escribe el nuevo valor de disponible"))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro{id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)

# Parte de los usuarios

def ver_usuario():
    try:
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()
        print("=== Usuarios en la biblioteca ===")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("------------------------------")
                print(
                    f"ID: {usuario.id}, Nombre {usuario.nombre},"
                    f"Matricula: {usuario.matricula}, Carrera: {usuario.carrera},"
                    f"Correo: {usuario.correo}"
                )
                print("--------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_usuario():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    matricula = input("Escribe la matricula del usuario: ")
    carrera = input("Escriba la carrera del nuevo usuario: ")
    correo = input("Escriba el correo del nuevo usuario")
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.insertar(usuario)
        print("Insercción realizada con exito")
    except Exception as e:
        print("Errror al insertar un nuevo usuario")
        print(e)

def actualizar_usuario():
    print("Seleciona el usuario a actualizar")
    try:
        usuario_dao= UsuarioDAO()
        ver_usuario()
        id = int(input("Escribe el id del usuario a actualizar"))
        nombre = input("Escribe el nuevo nombre del usuario")
        matricula = input("Escribe la nueva matricula del usuario")
        carrera = input("Escribe la nueva carrera del usuario")
        correo = input("Escribe el nuevo correo del usuario")
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.actualizar(usuario)
        print(f"El usuario{id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un usuario")
        print(e)

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles:")
        ver_usuario()
        id = input("Escribe el id del usuario a eliminar: ")
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)


def menu_libros():

    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Selecciona una opción (1-4)"))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario ya existente")
    print("4. Eliminar un usuario existente")
    opcion = int(input("Selecciona una opción (1-4)"))

    match opcion:
        case 1:
            ver_usuario()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()

def main():

    try:
            print("=== BIBLIOTECA UNIVERSITARIA ===")
            print("1.Gestionar Libros")
            print("2.Gestionar Usuarios")

            opcion = int(input("Seleccionar una opción general (1-2): "))
            match opcion:
                case 1:
                    menu_libros()
                case 2:
                    menu_usuarios()
                case _:
                    print("Opcion no valida.")
    except ValueError:
                print("Por favor, introduce un número válido.")



if __name__=="__main__":
    main()