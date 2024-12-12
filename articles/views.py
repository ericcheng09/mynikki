from django.shortcuts import render
from articles.models import Article

# Create your views here.
def show(request):
    articles = Article.objects.all()
    results = []
    for a in articles:
        results.append(
            {'date': a.date,
            'content': a.content,
            'create_at': a.create_at,
            'update_at': a.update_at}
        )
    return render(request, 'articles/show.html', {'results': results})