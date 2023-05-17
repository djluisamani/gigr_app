from django.urls import path
from . import views

urlpatterns = [
    path('gigs/', views.GigList.as_view()),
    path('gigs/<int:pk>/', views.GigDetail.as_view()),
    path('payments/', views.PaymentList.as_view()),
    path('payments/<int:pk>/', views.PaymentDetail.as_view()),
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('', views.splash, name='splash'),
]
