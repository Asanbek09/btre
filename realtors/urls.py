from django.urls import path
from . import views

app_name = "realtors"

urlpatterns = [
    path('', views.index, name='realtors'),
    path('<int:realtor_id>', views.realtor, name='realtor'),
]