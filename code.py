import tkinter as tk
from PIL import Image, ImageTk
label_resultado = None

def abrir_link(url):
    import webbrowser
    webbrowser.open(url)

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

# Cargar y mostrar la imagen
imagen = Image.open("/home/monux/ProyectoEmprendedorLeonel/codigo/logo.png")
imagen = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(root, image=imagen)
label_imagen.image = imagen  # Asegura que la imagen no sea eliminada por el recolector de basura
label_imagen.pack(side=tk.LEFT)  # Para colocar la imagen al costado derecho

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
    
    # Cargar y mostrar la imagen
    imagen = Image.open("/home/monux/ProyectoEmprendedorLeonel/codigo/logo.png")
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(root, image=imagen)
    label_imagen.image = imagen  # Asegura que la imagen no sea eliminada por el recolector de basura
    label_imagen.pack(side=tk.LEFT)  # Para colocar la imagen al costado derecho

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

    # Cargar y mostrar la imagen
    imagen = Image.open("/home/monux/ProyectoEmprendedorLeonel/codigo/logo.png")
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(ventana_opcion1, image=imagen)
    label_imagen.image = imagen  # Asegura que la imagen no sea eliminada por el recolector de basura
    label_imagen.pack(side=tk.LEFT)  # Para colocar la imagen al costado derecho

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

    # Cargar y mostrar la imagen
    imagen = Image.open("/home/monux/ProyectoEmprendedorLeonel/codigo/logo.png")
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(ventana_opcion2, image=imagen)
    label_imagen.image = imagen  # Asegura que la imagen no sea eliminada por el recolector de basura
    label_imagen.pack(side=tk.LEFT)  # Para colocar la imagen al costado derecho

    # Sección donde aparecerá la selección del nivel de estrés
    label_seleccion = tk.Label(ventana_opcion2, text="Nivel de Estrés:")
    label_seleccion.pack()

    # Variable para almacenar la selección del nivel de estrés
    seleccion_estres = tk.StringVar()

    # Agrega botones para los niveles de estrés
    niveles_estres = ["Nada Estresado", "Poco Estresado", "Estresado", "Muy Estresado", "Super Estresado"]
    for nivel_estres in niveles_estres:
        btn_nivel_estres = tk.Button(ventana_opcion2, text=nivel_estres, 
        command=lambda n=nivel_estres: mostrar_resultado(n, seleccion_estres))
        btn_nivel_estres.pack()

    # Botón para regresar al menú principal
    btn_regresar = tk.Button(ventana_opcion2, text="Regresar al Menú", command=mostrar_menu)
    btn_regresar.pack()

    # Botón para salir de la aplicación
    btn_salir = tk.Button(ventana_opcion2, text="Salir", command=root.destroy)
    btn_salir.pack()

def mostrar_ventana_opcion3():
    ventana_opcion3 = tk.Toplevel(root)
    ventana_opcion3.title("Ventana de Meditaciones")
    # Agrega elementos a la ventana de Meditaciones según tus necesidades

    # Cargar y mostrar la imagen
    imagen = Image.open("/home/monux/ProyectoEmprendedorLeonel/codigo/logo.png")
    imagen = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(ventana_opcion3, image=imagen)
    label_imagen.image = imagen  # Asegura que la imagen no sea eliminada por el recolector de basura
    label_imagen.pack(side=tk.LEFT)  # Para colocar la imagen al costado derecho

    # Botones para meditaciones (hipervínculos)
    meditacion1_button = tk.Button(ventana_opcion3, text="Meditación 1", 
                                   command=lambda: abrir_link("https://cultivarlamente.com/meditaciones-guiadas/"))
    meditacion1_button.pack()

    meditacion2_button = tk.Button(ventana_opcion3, text="Meditación 2", 
                                   command=lambda: abrir_link("https://kensho.life/meditaciones-guiadas"))
    meditacion2_button.pack()

    meditacion3_button = tk.Button(ventana_opcion3, text="Meditación 3", 
                                   command=lambda: abrir_link("https://www.prana.es/meditaciones-guiadas.html"))
    meditacion3_button.pack()
    
    # Botón para regresar al menú principal
    btn_regresar = tk.Button(ventana_opcion3, text="Regresar al Menú", command=mostrar_menu)
    btn_regresar.pack()

    # Botón para salir de la aplicación
    btn_salir = tk.Button(ventana_opcion3, text="Salir", command=root.destroy)
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
