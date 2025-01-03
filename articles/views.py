from django.shortcuts import render
from django.utils.timezone import make_aware
from datetime import datetime
from articles.models import Article
from django.http import HttpResponseNotAllowed, Http404

SORT_BY_OPTIONS = ['id', 'create_at', 'update_at']

# Create your views here.
def show_all(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed()
    
    sort_by = request.GET.get('sort_by', 'id')
    sort_by = sort_by.lower()
    if sort_by not in SORT_BY_OPTIONS:
        sort_by = 'id'
     
    articles = Article.objects.all()
    results = []

    for a in articles:
        results.append(
            {
            'id': a.id,
            'date': a.date,
            'content': a.content[:20] + '...',
            'create_at': make_aware(datetime.fromtimestamp(a.create_at)),
            'update_at': make_aware(datetime.fromtimestamp(a.update_at))}
        )
    
    results = sorted(results, key= lambda r: r[sort_by], reverse=True)    
    return render(request, 'articles/list.html', {'results': results})


def detail(request, id):
    article = Article.objects.get(pk=id)
    if article:
        r = {
            'date': article.date,
            'content': article.content,
            'create_at': make_aware(datetime.fromtimestamp(article.create_at)),
            'update_at': make_aware(datetime.fromtimestamp(article.update_at))
            }
        return render(request, 'articles/show.html', r)
  
    return Http404()