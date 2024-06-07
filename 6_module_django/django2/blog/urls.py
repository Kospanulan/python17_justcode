from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostAPIView.as_view()),
    path('<int:post_id>/', views.detail),

]
