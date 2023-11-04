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
    context : dict = {}
    return render(request, 'seccion02.html', context)