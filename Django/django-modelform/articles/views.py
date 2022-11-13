from .forms import ArticleForm, CommentForm
from .models import Article
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # redirect랑 동일한 서버코드(302)

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/form.html", context=context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            # POST : input 값 가져와서, 검증하고, DB에 저장
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                article_form.save()
                messages.success(request, "글이 수정되었습니다.")
                return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            article_form = ArticleForm(instance=article)
        context = {
            "article_form": article_form,
        }
        return render(request, "articles/form.html", context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다.
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("articles:detail", article.pk)


def detail(request, pk):
    # 특정 글을 가져온다.
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # commit=False => 멈춰!
        comment = comment_form.save(commit=False)
        comment.article = article
        # 코맨트 다는 유저가 맞는지
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # if article.like_users.filter(id=request.user.id).exists():
    # 위 코드는 exists로 article.like_users안에 request.user.id가 있는지 찾는다.
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고
        article.like_users.add(request.user)
    # 상세페이지로 redirect
    return redirect("articles:detail", pk)
