from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from django.shortcuts import render
from . import forms
import hashlib
# Create your views here.


def index(request):

    return render(request, 'login/login.html')


def logout(request):
    if request.session.get('is_login', None):
        return redirect('/blog/')
    request.session.flush()
    return render(request, 'blog/index.html', locals())

def loginto(request):
        if request.session.get('is_login',None):
            return redirect('/blog/')
        if request.method == "POST":
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            message = "所有字段都必须填写！"
            if username and password:  # 确保用户名和密码都不为空
                username = username.strip()
                # 用户名字符合法性验证
                # 密码长度验证
                # 更多的其它验证.....
                try:
                    user = models.User.objects.get(name=username)
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect('/blog/')
                    else:
                        message = "密码不正确！"
                except:
                    message = "用户名不存在！"
            return render(request, 'login/login.html', {"message": message})
        return render(request, 'login/login.html')


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/blog/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def hash_code(s,salt='login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encodde())
    return h.hexdigest()