from django.urls import path

from .views import *

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
]
