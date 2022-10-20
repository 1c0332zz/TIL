from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


# def is_odd_even(request, _number):
#     context = {"number": _number}

#     return render(request, "is-odd-even.html", context)
def check(request, _number):
    num = _number
    if num == 0:
        check = 0
    elif num % 2 == 0:
        check = "짝수"
    else:
        check = "홀수"
    context = {"num": num, "check": check}
    return render(request, "is-odd-even.html", context)


def calculate(request, _number, __number):
    num = _number
    num2 = __number
    context = {
        "plus": num + num2,
        "minus": num - num2,
        "multiply": num * num2,
        "divide": num // num2,
    }

    return render(request, "calculate.html", context)
