from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [

    path('', palestrante, name='palestrante'),

    path('palestrante_list/', palestranteList.as_view(), name='palestrante_list'),
    path('palestrante_create/', palestranteCreate.as_view(), name='palestrante_create'),
    path('palestrante_detail/<int:pk>', palestranteDetail.as_view(), name='palestrante_detail'),
    path('palestrante_update/<int:pk>/', palestranteUpdate.as_view(), name='palestrante_update'),
    path('palestrante_delete/<int:pk>/', palestranteDelete.as_view(), name='palestrante_delete'),

]