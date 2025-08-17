from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
# Create your views here.

# clase based views IMPLEMENTATION


# class ReviewView(FormView):
class ReviewView(CreateView):
    template_name = "reviews/review.html"
    success_url = "/reviews/thank-you"
    form_class = ReviewForm
    model = Review
    # fields = ["user_name", "review_text", "rating"]

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     # review = Review.objects.get(pk=1)
    #     # form = ReviewForm(request.POST, instance=review)

    #     if form.is_valid():
    #         # form = form.cleaned_data

    #         # como ya es un formulario basado en un modelo al utilizar el metodo save automaticamente se guardaran lso valores en la base de datos, con la implementacion anterior esto no era posible
    #         form.save()

    #         return HttpResponseRedirect("/reviews/thank-you")


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
# def thank_you(request):
#     return render(request, "reviews/thank_you.html", {
#         "has_error": False,

#     })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "koso"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)
        return data


class SingleReviewCiew(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        # favorite_id = request.session["favorite_review"]
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(
            loaded_review.id) if favorite_id else False
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
