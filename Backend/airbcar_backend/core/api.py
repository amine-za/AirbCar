from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]