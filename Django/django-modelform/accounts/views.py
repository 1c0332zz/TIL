from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationForm

# from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ModelForm의 save메서드의 리턴값은 해당 모델의 인스턴스다
            auth_login(request, user)  # 바로 로그인
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


def login(request):
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user객체를 인자로 받음
            # user 객체는 ㅇㄷ? 바로 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            # http://127.0.0.1:8000/accounts/login/?next=/articles/1/update/
            # request.GET.get('next') : /articles/1/update/
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # auth_login(request, user) 도 사용할 수 있지만 @login_required로 대체
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def logout(request):
    auth_logout(request)
    messages.warning(request, "로그아웃 하였습니다.")
    return redirect("articles:index")


@login_required
def follow(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가!
    # user = get_user_model().objects.get(pk=pk)
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        # 강제로 사이트로 들어올려고 하면!
        messages.warning(request, "스스로 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    if request.user in user.followers.all():
        # (이미) 팔로우 상태이면, '팔로우 취소'버튼을 누르면 삭제 (remove)
        user.followers.remove(request.user)
    else:
        # 팔로우 상태가 아니면, '팔로우'를 누르면 추가 (add)
        user.followers.add(request.user)
    return redirect("accounts:detail", pk)
