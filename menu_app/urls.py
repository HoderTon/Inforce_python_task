from django.urls import path
from . import views
urlpatterns = [
    path('menu', views.MenuList.as_view())
    #path('add_menu/<int:pk>', )
]