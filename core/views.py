from django.shortcuts import render, HttpResponse

# Контекст в шаблонах, ссылки

def main_view(request):
    return render(request, 'main_page.html', {})

def contacts_view(request):
    return render(request, 'contacts_page.html', {})



# reguest - запрос
# responce - ответ

# return HttpResponse(f"{request.__dict__}")

# def test(request):
#     return render(request, 'index.html', {})

# def test2(request):
#     return HttpResponse("Саламчик!")

# def test3(request):
#     return HttpResponse("Привет")

# def second_test(request):
#     return render(request, 'second.html', {})


