from django.urls import include, path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
urlpatterns = [
    path('article/', include('articles.urls')),
    path('', views.index),  # 配置当访问index/时去调用views下的index方法
]
