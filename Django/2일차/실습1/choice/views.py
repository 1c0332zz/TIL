from django.shortcuts import render
import random
# Create your views here.

def index(request):
    names = ['닭가슴살', '볶음밥', '샐러드', '고구마']
    imges = [
        'https://img.danawa.com/prod_img/500000/917/763/img/14763917_1.jpg?shrink=330:330&_v=20210716134451',
        'https://recipe1.ezmember.co.kr/cache/recipe/2021/12/08/8c6d637166ad45c8af715ea09e9f7cac1.jpg',
        'https://health.chosun.com/site/data/img_dir/2021/05/06/2021050601029_0.jpg',
        'https://t1.daumcdn.net/cfile/tistory/2361853557BEA99F17',
    ]
    name = random.choice(names)
    context = {

    }

    return render(request, 'today-dinner', context)


