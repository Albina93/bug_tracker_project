from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_ticket/', views.add_ticket_view, name="add_ticket"),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view, name="ticket_details"),
    path('assign_ticket/<int:ticket_id>/', views.assign_ticket_view, name="assign_details"),
    path('invalid_ticket/<int:ticket_id>/', views.invalid_ticket_view, name="invalid_details"),
    path('complete_ticket/<int:ticket_id>/', views.complete_ticket_view, name="complete_details"),
    path('new_ticket/<int:ticket_id>/', views.new_ticket_view, name="new_ticket__details"),
    path('ticket/<int:ticket_id>/edit', views.edit_ticket_view, name="edit_page"),
    path('user/<str:user_name>/', views.user_detail_view, name="user_details"),
    path('login/', views.login_view, name="loginpage"),
    path('logout/', views.logout_view, name="logoutpage"),

]