from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apiSteam.apps.games.presentation.views.game_views import GameListCreateView, GameDetailView

router = DefaultRouter()
urlpatterns = [
    path('', GameListCreateView.as_view(), name='game-list-create'),
    path('<int:game_id>/', GameDetailView.as_view(), name='game-detail'),
    path('', include(router.urls)),
]