from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("all", views.ReviewsListView.as_view()),
    path("favorite", views.AddFavoriteView.as_view()),
    path("<int:pk>", views.SingleReviewCiew.as_view())
    # path("thank-you", views.thank_you)
]
