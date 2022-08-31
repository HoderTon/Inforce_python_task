from django.urls import path
from . import views

urlpatterns = [
    path('create_restaurant', views.RestaurantCreate.as_view()),  # Add new restaurant (POST)

    # Checkout all the menus (GET) and their votes.
    path('menus', views.MenuList.as_view()),  # Or CREATE one (POST).
    path('menus/<int:pk>', views.MenuRetrieveDestroy.as_view()),  # Checkout particular menu (GET) or delete (DELETE) it
    path('menus/<int:pk>/vote', views.VoteCreate.as_view()),  # Vote for particular menu (POST)
    path('menus/today_menus', views.MenuTodayList.as_view()),  # Checkout menus for today (GET)
    path('menus/most_voted', views.MostVotedMenu.as_view())  # Get most voted menu (GET) for today

]
