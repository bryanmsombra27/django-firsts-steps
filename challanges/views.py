from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    # "december": "In December, learn ",
    "december": None,
}


def index(request):
    months = list(monthly_challanges.keys())

    return render(request, "challanges/index.html", {"months": months})


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
    print("Mes recibido:", month)
    try:
        challange_text = monthly_challanges[month]
        # response_data = f"<h1>{challange_text}</h1>"
        # response_data = render_to_string("challanges/challange.html")
        # return HttpResponse(response_data)
        print(challange_text, "MES ACTUAL")

        return render(request, "challanges/challange.html", {"challange": challange_text, "month": month})
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


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
