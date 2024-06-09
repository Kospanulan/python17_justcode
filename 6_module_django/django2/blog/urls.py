from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view()),
    path('<int:pk>/', views.PostRetrieveAPIView.as_view()),

]
