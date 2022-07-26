from datetime import datetime
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template
import datetime 

def template(request):
    
    hoy = datetime.datetime.now
    nota = [6,4,7,2,8,1,9]
    nombre = "Jejo"

    with open(r"C:\Users\Juan\Desktop\django\my_site\index.html") as f:

        plantilla = Template(f.read())
    contexto= Context({"data":hoy,"nota":nota,"nombre":nombre})

    return HttpResponse(plantilla.render(contexto))