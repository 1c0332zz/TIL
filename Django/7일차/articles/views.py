from django.shortcuts import render, redirect
from articles.models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    # 게시글에서 꺼내와서(쿼리셋 => Article객체를 가진)
    articles = Article.objects.order_by("-pk")
    # templates에 뿌려준다.
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         "article_form": article_form,
#     }
#     return render(request, "articles/new.html", context=context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/new.html", context=context)  # invalid
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Article.objects.create(title=title, content=content)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        "article": article,  # 사용자 인풋을 다 받아서, 검증까지해서 에러메시지를 만든 article_form
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    # GET : Form을 제공
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)
