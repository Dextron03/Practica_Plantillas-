from django.shortcuts import render

def first_seccion(request):
    context : dict = {}
    return render(request, 'seccion01.html', context) 
