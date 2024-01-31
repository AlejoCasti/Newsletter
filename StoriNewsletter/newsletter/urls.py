from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateNewsletter.as_view(), name='create'),
    path('delete/<str:id>/', views.DeleteNewsletter.as_view(), name='delete'),
    path('send/', views.SendNewsletter.as_view(), name='send'),
    path('list/', views.GetNewsletters.as_view(), name='list-newsletter'),
    path('unsubscribe/<str:token>/', views.UnsubscribeNewsletter.as_view(), name='unsubscribe'),
    path('statistics/', views.Statistics.as_view(), name="statistics"),
]
