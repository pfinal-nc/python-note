from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import Http404
# Create your views here.
from .models import Articles
import time


def index(request):
    articles_list = Articles.objects.order_by('-add_time')
    context = {'articles_list': articles_list}
    return render(request, 'articles/article_list.html', context)
    # return render(request, 'articles/article_list.html')
    # return HttpResponse(articles_list_content)


def detail(request, articles_id):
    try:
        artilce = Articles.objects.get(pk=articles_id)
    except Articles.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'articles/article_detail.html', {'artilce': artilce})
