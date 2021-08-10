from django.urls import path
from client_api import views


urlpatterns = [
    # SET/GET profile data
    path('initial/', views.Initial.as_view(), name='Initial')

]
