from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apiSteam.apps.user.presentation.views.user_views import UserCreateView, UsersViewSet
from apiSteam.apps.user.presentation.views.user_profile_views import UserProfileView

router = DefaultRouter()
router.register(r'', UsersViewSet, basename='users')
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]