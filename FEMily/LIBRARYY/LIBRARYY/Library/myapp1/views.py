from django.shortcuts import render

from myapp1.models import News, Books


def index_page(request):
    all_news = News.objects.all()
    return render(request, 'index.html', context={'data3': all_news})

def katalog_page(request):
    all_books = Books.objects.all()
    return render(request, 'katalog.html', context={'data': all_books})

def kontakt_page(request):

    return render(request, 'kontakt.html')
