from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("menu-items/", views.MenuItemsListView.as_view()),
    path("menu-items/<int:pk>", views.MenuItemView.as_view()),
    path("tables-booking/", views.BookingListView.as_view()),
    path("tables-booking/<int:pk>", views.BookingItemView.as_view()),
]       
