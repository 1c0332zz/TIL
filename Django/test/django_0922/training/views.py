from django.shortcuts import render

# Create your views here.

# HTTP : 요청(request)을 하면 무언가를 응답(response)하는 방식
# index 함수 선언 정의
def index(request):
    
    return render(request, 'index.html')

def template(request):
    _number = 1
    context = {
        'number' : _number,
    }
    return render(request, 'template.html', context)

def template2(request):
    number = 2
    context = {
        'numbers' : number, 
    }
    return render(request, 'template.html', context)
