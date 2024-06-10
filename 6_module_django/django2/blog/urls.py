from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view()),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view()),
]

"""

GET            /posts/ - возвращает список постов
POST           /posts/ - Добавляет один новый пост

GET            /posts/1/ - Возвращает одну запись
DELETE         /posts/1/ - Удаляет одну запись
PUT / PATCH    /posts/1/ - Обновляет одну запись

"""