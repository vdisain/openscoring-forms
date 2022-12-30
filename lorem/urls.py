from django.urls import path
from .views import LoremFormView, LoremThankYouView

app_name = "lorem"

urlpatterns = [
    path('', LoremFormView.as_view(), name="form"),
    path('thank-you', LoremThankYouView.as_view(), name="thank_you"),
]