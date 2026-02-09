from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apiSteam.apps.library.presentation.views.library_views import UserLibraryView

router = DefaultRouter()
urlpatterns = [
    path("", UserLibraryView.as_view(), name="user-library"),
    path('', include(router.urls)),
]