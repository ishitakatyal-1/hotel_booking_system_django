from django.urls import path, include
from .views import GuestsView, GuestDateFiilterView

urlpatterns = [
    path('guests', GuestsView.as_view()),
    path('guestsdatefilter', GuestDateFiilterView.as_view())
]
