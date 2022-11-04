## 1:N(User - Comment)

### 개요

* User(1) - Comment(N) 
* User 모델과 Comment 모델 간 관계 설정 
* “0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음”

## 모델 관계 설정

### Comment와 User간 모델 관계 설정 (1/2)

![image-20221031230402919](readme.assets/image-20221031230402919.png)

* Comment 모델에 User 모델을 참조하는 외래 키 작성

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

### Migration 진행

* 이전에 User와 Article 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새 로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요

```bash
$ python manage.py makemigrations
$ python manage.py migrate

# comment 테이블 스키마 변경 및 확인
```

## CREATE

* 인증된 회원의 댓글 작성 구현하기
* 작성하기 전 로그인을 먼저 진행한 상태로 진행

### CommentForm

* CommentForm 출력을 확인해보면 create 템플릿에서 불필요한 필드(user)가 출력 됨 
* user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용해야 함
* CommentForm의 출력 필드 수정

```python
# articles/forms.py
class CommentForm(forms.ModelForm):
class Meta:
    model = Comment
    exclude = ('article', 'user',)
```

* 댓글 작성 시 NOT NULL constraint failed: articles_comment.user_id 에러 발생
* “NOT NULL 제약 조건이 실패했다. articles_comment 테이블의 user_id 컬럼에서”
* 댓글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락 되었기 때문
* 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

```python
# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)	
```

### READ

* detail 템플릿에서 각 게시글의 작성자 출력

```html
<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
...
<h4>댓글 목록</h4>
...
<ul>
	{% for comment in comments %}
		<li>
			{{ comment.user }} - {{ comment.content }}
			<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            	{% csrf_token %}
            	<input type="submit" value="DELETE">
            </form>
        ...
```

### DELETE

* 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제 할 수 있도록 함

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
    	comment.delete()
    return redirect('articles:detail', article_pk)
```

* 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

```html
<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
  ...
  <ul>
    {% for comment in comments %}
     <li>
    	{{ comment.user }} - {{ comment.content }}
    	{% if request.user == comment.user %}
    		<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
    		{% csrf_token %}
    		<input type="submit" value="DELETE">
   		</form>
    {% endif %}
...
```

