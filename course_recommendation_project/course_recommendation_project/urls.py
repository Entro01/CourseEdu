from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('recommendations/', views.recommend_courses, name='recommend_courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('attention_metrics/', views.attention_metrics, name='attention_metrics'),
]
