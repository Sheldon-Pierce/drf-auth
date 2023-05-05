from django.urls import path
from games.views import GamesList

urlpatterns = [
    path('', GamesList.as_view(), name='list_view')
]