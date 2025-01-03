from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name='all_article'),
    path('<int:id>', views.detail, name='article_detail'),
]