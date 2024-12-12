from django.shortcuts import render

# Create your views here.
def show(request):
    results = [
        {'date': 'test',
         'content': 'Test content',
         'create_at': 123,
         'update_at': 123}
    ]
    return render(request, 'articles/show.html', locals())