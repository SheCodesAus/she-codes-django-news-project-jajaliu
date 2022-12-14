from django.urls import path 
from .views import CreateAccountView, UserProfileView, AuthorListView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/authors/', AuthorListView.as_view(), name = "authors"),
    path('profile/<int:pk>/', UserProfileView.as_view(), name = "profile"),
    path('profile/<str:slug>/', UserProfileView.as_view(), name = "profile"),
]