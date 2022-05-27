from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return render(request, 'index.html')


class UserClass:
    def __init__(self, request):
        data = request.POST.get('data', None)
        print(data)
        return (data)


def sign_up(request):
    if request.method == 'POST':
        data = UserClass()
        print(data.email)
        password = request.POST.get('data.password', None)

        # if email.find('@') == -1:
        #     return HttpResponse("이메일 형식 에러")
        # elif len(password) < 8:
        #     return HttpResponse("비밀번호 길이 에러")
