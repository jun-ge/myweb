from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from blog1.models import User


def index(request):
    article = models.Ar
    return render(request, "blog1/index.html",)



def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    # SELECT  * FROM  T_USER  WHERE USERNAME = 'XIAOMING'
    try:
        user = User.objects.get(username=username)
        if user:
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('账号不存在')
    except:
        return HttpResponse('链接失败')


# restful   服务器接口设计的规范
def register(request):
    # 获取客服端端通过get请求发送过来的数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    phone = request.GET.get('phone')
    # insert into
    # user = User(username='xiaoming', password='123456')
    result = '注册失败'
    try:
        user = User.objects.filter(username=username)
        if user:
           return HttpResponse('用户已存在')
        else:
            User.objects.create(username=username, password=password)
            return HttpResponse('注册成功')
    except:
        pass
    return HttpResponse(result)
