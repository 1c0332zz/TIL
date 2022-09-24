from django.shortcuts import render
import random
# Create your views here.

def index(request):

    return render(request, 'today-dinner.html')

def today_dinner(request):
    arr = [
        {'name': '닭가슴살', 'src':'https://img.danawa.com/prod_img/500000/917/763/img/14763917_1.jpg?shrink=330:330&_v=20210716134451'},
        {'name': '볶음밥', 'src': 'https://recipe1.ezmember.co.kr/cache/recipe/2021/12/08/8c6d637166ad45c8af715ea09e9f7cac1.jpg'},
        {'name': '샐러드', 'src': 'https://health.chosun.com/site/data/img_dir/2021/05/06/2021050601029_0.jpg'},
        {'name': '고구마', 'src': 'https://t1.daumcdn.net/cfile/tistory/2361853557BEA99F17'}, 
    ]

    context = {
        'arr' : random.choice(arr)
    }

    return render(request, 'today-dinner.html', context)

def lotto(request):
    
    lotto_list = []
    for i in range(5):
        lotto = random.sample(range(1, 46), 6)
        lotto_list.append(lotto)
    
    context = {
        "lotto_list": lotto_list 
    }

    return render(request, "lotto.html", context)
