from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from .models import Review
# Create your views here.

# clase based views IMPLEMENTATION


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        # review = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            # form = form.cleaned_data

            # como ya es un formulario basado en un modelo al utilizar el metodo save automaticamente se guardaran lso valores en la base de datos, con la implementacion anterior esto no era posible
            form.save()

            return HttpResponseRedirect("/reviews/thank-you")


# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         # review = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=review)

#         if form.is_valid():
#             # form = form.cleaned_data

#             # como ya es un formulario basado en un modelo al utilizar el metodo save automaticamente se guardaran lso valores en la base de datos, con la implementacion anterior esto no era posible
#             form.save()

#             return HttpResponseRedirect("/reviews/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })
    # return render(request, "reviews/review.html")


# generic implementation
def thank_you(request):
    return render(request, "reviews/thank_you.html", {
        "has_error": False,

    })
