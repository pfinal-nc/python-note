from django.urls import path
from . import views
app_name = 'article'
urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='article_list'),
]
