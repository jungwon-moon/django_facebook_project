from django.shortcuts import render, redirect
from facebook.models import Article, Page

# Create your views here.
count = 0


def play(request):
    return render(request, 'play.html')


def play2(request):
    name = '정원'
    global count
    count += 1
    age = 20

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['비가 온다 태풍이다 (9월 14일)', '오늘은 날씨가 맑았다. - 9월 13일',
             '일요일이다. 9월 12일에 작성']
    return render(request, 'play2.html', {'name': name, 'cnt': count, 'age': status, 'diary': diary})


def my_profile(request):
    return render(request, 'profile.html')


def event(request):
    name = '정원'
    global count
    count += 1
    age = 20

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    if count % 2 == 1:
        lottery = "당첨"
    else:
        lottery = "꽝!!"

    return render(request, 'event.html', {'name': name, 'cnt': count, 'age': status, 'lottery': lottery})


def fail(request):
    return render(request, 'fail.html')


def help(request):
    return render(request, 'help.html')


def warn(request):
    return render(request, 'warn.html')


def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail_feed.html', {'feed': article})


def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})


def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and \
                request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )
            return redirect(f'/feed/{new_article.pk }')
    return render(request, 'new_feed.html')


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'remove_feed.html', {'feed': article})


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'edit_feed.html', {'feed': article})
