from django.urls import path, include
from . import views


# urlpatterns = [
#     path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', views.RegisterView.as_view(), name='auth_register'),
#     path('', views.getRoutes)
# ]

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('authVerify/', views.UserIdRespone.as_view())
    # path('register/', views.RegistrationAPIView.as_view()),
    # path('login/', views.LoginAPIView.as_view()),
]