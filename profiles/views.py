from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# SOLO FUNCIONA CON .JPG


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class ProvileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profile"


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         print(request.FILES["user_image"], "KOSO")
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # store_file(request.FILES["image"])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profile")
#         else:
#             return render(request, "profiles/create_profile.html", {
#                 "form": form
#             })
