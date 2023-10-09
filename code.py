import tkinter as tk
label_resultado = None

def validar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Aquí puedes realizar la validación del usuario y la contraseña
    # Por ejemplo, comparando con una base de datos o credenciales almacenadas.

    if usuario == "usuario" and contraseña == "contraseña":
        label_resultado.config(text="Inicio de sesión exitoso")
        mostrar_menu()
        root.destroy()
    else:
        label_resultado.config(text="Credenciales incorrectas")

def registrar():
    # Aquí puedes implementar la lógica para registrar un nuevo usuario
    # por ejemplo, almacenar el nuevo usuario y contraseña en una base de datos.
    label_resultado.config(text="Nuevo usuario registrado")

def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión y Registro")

# Etiquetas y campos de entrada
label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(root, show="*")
entry_contraseña.pack()

# Botones de inicio de sesión, registro y salir
btn_login = tk.Button(root, text="Iniciar Sesión", command=validar_login)
btn_login.pack()

btn_registrar = tk.Button(root, text="Registrar", command=registrar)
btn_registrar.pack()

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.pack()

# Etiqueta para mostrar el resultado del inicio de sesión o registro
label_resultado = tk.Label(root, text="")
label_resultado.pack()


def mostrar_menu():
    # Limpiar la ventana de elementos anteriores
    for widget in root.winfo_children():
        widget.destroy()
    
    # Crear elementos del menú
    label_menu = tk.Label(root, text="¡Bienvenido a PyCalm!")
    label_menu.pack()

    btn_opcion1 = tk.Button(root, text="Animo", command=opcion1)
    btn_opcion1.pack()

    btn_opcion2 = tk.Button(root, text="Estres", command=opcion2)
    btn_opcion2.pack()

    btn_opcion3 = tk.Button(root, text="Meditaciones", command=opcion3)
    btn_opcion3.pack()

    btn_logout = tk.Button(root, text="Cerrar Sesión", command=cerrar_sesion)
    btn_logout.pack()

def mostrar_ventana_opcion1():
    ventana_opcion1 = tk.Toplevel(root)
    ventana_opcion1.title("Ventana de Animo")
    # Agrega elementos a la ventana de Animo según tus necesidades

    # Sección donde aparecerá la selección del botón
    label_seleccion = tk.Label(ventana_opcion1, text="Selección:")
    label_seleccion.pack()

    # Variable para almacenar la selección del botón
    seleccion = tk.StringVar()

    # Agrega botones para las emociones
    emociones = ["Feliz", "Triste", "Enojado", "Ansioso", "Estresado"]
    for emocion in emociones:
        btn_emocion = tk.Button(ventana_opcion1, text=emocion, command=lambda e=emocion: mostrar_resultado(e))
        btn_emocion.pack()

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(ventana_opcion1, text="Regresar al Menú", command=mostrar_menu)
    btn_regresar.pack()

    # Botón para salir de la aplicación
    btn_salir = tk.Button(ventana_opcion1, text="Salir", command=root.destroy)
    btn_salir.pack()

def mostrar_ventana_opcion2():
    ventana_opcion2 = tk.Toplevel(root)
    ventana_opcion2.title("Ventana de Estres")
    # Agrega elementos a la ventana de Estres según tus necesidades

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(ventana_opcion1, text="Regresar al Menú", command=mostrar_menu)
    btn_regresar.pack()

    # Botón para salir de la aplicación
    btn_salir = tk.Button(ventana_opcion1, text="Salir", command=root.destroy)
    btn_salir.pack()

def mostrar_ventana_opcion3():
    ventana_opcion3 = tk.Toplevel(root)
    ventana_opcion3.title("Ventana de Meditaciones")
    # Agrega elementos a la ventana de Meditaciones según tus necesidades

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(ventana_opcion1, text="Regresar al Menú", command=mostrar_menu)
    btn_regresar.pack()

    # Botón para salir de la aplicación
    btn_salir = tk.Button(ventana_opcion1, text="Salir", command=root.destroy)
    btn_salir.pack()

def opcion1():
    # Lógica para la opción 1
    for widget in root.winfo_children():
        widget.destroy()
    mostrar_ventana_opcion1()
    label_menu.config(text="Opción 1 seleccionada")

def opcion2():
    # Lógica para la opción 2
    for widget in root.winfo_children():
        widget.destroy()
    mostrar_ventana_opcion2()
    label_menu.config(text="Opción 2 seleccionada")

def opcion3():
    # Lógica para la opción 3
    for widget in root.winfo_children():
        widget.destroy()
    mostrar_ventana_opcion3()
    label_menu.config(text="Opción 3 seleccionada")


# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
