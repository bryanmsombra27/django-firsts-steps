from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challanges = {
    "january": "In January, learn Python",
    "february": "In February, learn Django",
    "march": "In March, learn JavaScript",
    "april": "In April, learn HTML",
    "may": "In May, learn CSS",
    "june": "In June, learn ",
    "july": "In July, learn ",
    "august": "In August, learn ",
    "september": "In September, learn ",
    "october": "In October, learn ",
    "november": "In November, learn ",
    "december": "In December, learn ",
}


def index(request):
    return HttpResponse("this works")


def february(request):
    return HttpResponse("this works in february")


def march(request):
    return HttpResponse("learm django")


def monthly_chanllange_by_number(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not valid")

    redirect_month = months[month - 1]

# USANDO EL PARAMETRO NAME DE LA FUNCION PATH, USAMOS EL ARGUMENTO ARGS PARA QUE CON LA FUNCIUON REVERSE PUEDA GENERAR AUTOMATICAMENTE EL URL DE REDIRECCION SIN NOSOTROS TENER QUE CONSTRUIRLO MANUALMENTE REEMPLAZANDO LA RUTA '/challanges/' + redirect_month y generandola automaticamente
    redirect_path = reverse("monthly_challange", args=[redirect_month])

    # return HttpResponseRedirect('/challanges/' + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        response_data = f"<h1>{challange_text}</h1>"
    except:
        return HttpResponseNotFound("<h1> This month is not valid </h1>")

    return HttpResponse(response_data)


def monthly_list(request):
    months = list(monthly_challanges.keys())
    list_items = ""

    for i in months:
        monthPath = reverse("monthly_challange", args=[i])
        # list_items += f"<li><a href='/challanges/{i}'>{i}</a></li>"
        list_items += f"<li><a href='{monthPath}'>{i}</a></li>"

    response_data = f'''
    <ul> 
            {list_items}
    </ul>

'''

    return HttpResponse(
        response_data

    )

    # return JsonResponse(months, safe=False
