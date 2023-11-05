from django.shortcuts import render
import datetime

def first_seccion(request):
    lenguajes : list = ["Python", "SQL"]
    full_name : str = "Braily Roman Seberino"
    profeccion : str = "Desarrollador de Software Back-end"
    actual_year = datetime.datetime.now().year
    
    context : dict = {
        'descrip':f"¡Hola, soy {full_name}! 👨‍💻 {profeccion} 👨‍💻, apasionado por la tecnología y la manera en la que es posible aportar valor con la misma. Mi enfoque principal es el desarrollo de soluciones impactantes utilizando {''.join(lenguajes[0])}, y también tengo experiencia en el uso de bases de datos relacionales a través de {''.join(lenguajes[1])}. Estoy dispuesto a explorar otras tecnologías y aprender y adoptarlas según sea necesario. Mi objetivo es formar parte de un equipo cuyo propósito también sea mejorar constantemente la experiencia del usuario.",
        'nombre':full_name,
        'year': actual_year,
        'correo':'brailyrs03@gmail.com',
        'numero':'(829) 5329522'
                      }
    return render(request, 'seccion01.html', context) 

def second_seccion(request):
    actual_year = datetime.datetime.now().year
    proyectos = { 
        "TerminalCRUD":"Este proyecto se centra en la creación de una aplicación de línea de comandos en Python que proporciona una interfaz de usuario para interactuar con una base de datos SQLite. La aplicación está diseñada para llevar a cabo operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una base de datos SQLite existente.",
        "Random_Password_Generator":"Este es un programa de Python que te permite generar contraseñas aleatorias con opciones de configuración. Puedes determinar la longitud de la contraseña, incluir o excluir letras mayúsculas, números y símbolos.",
        "Reto_Lenguaje_Hacker":"El programa solicita al usuario que ingrese un texto y luego realiza la conversión a lenguaje hacker utilizando una tabla de reemplazos específica. Puedes encontrar la tabla de reemplazos en el siguiente enlace: Tabla de Leet Speak.",
    }
    
    context : dict = {
        'proyectos':proyectos,
        'year': actual_year,
        'correo':'brailyrs03@gmail.com',
        'numero':'(829) 5329522'   
    }

    return render(request, 'seccion02.html', context)
