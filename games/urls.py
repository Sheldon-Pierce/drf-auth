from django.urls import path
from games.views import GamesList, GamesDetail

urlpatterns = [
    path('', GamesList.as_view(), name='list_view'),
    path('<int:pk>/', GamesDetail.as_view(), name='detail_view')
]