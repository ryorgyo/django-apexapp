from django.shortcuts import render
from .forms import LoginForm,NewAccountForm
# Create your views here.
def signin(request):
  form = LoginForm
  title = 'えぺふれんずにログイン'
  form_action = ''
  button_text = 'ログイン'
  a_boo = True
  a_href = 'signup'
  a_text = '新規登録はこちら'
  params = {
    'form':form,
    'title':title,
    'form_action':form_action,
    'button_text':button_text,
    'a_boo':a_boo,
    'a_href':a_href,
    'a_text':a_text,
  }
  return render(request,'myapp/index.html',params)

def signup(request):
  form = NewAccountForm
  title = 'アカウント新規作成'
  form_action = ''
  button_text = '新規登録'
  a_boo = False
  a_href = 'signin'
  a_text = 'ログインはこちら'
  params = {
    'form':form,
    'title':title,
    'form_action':form_action,
    'button_text':button_text,
    'a_boo':a_boo,
    'a_href':a_href,
    'a_text':a_text,
  }
  return render(request,'myapp/index.html',params)

def contact(request):
  form = LoginForm
  params = {
    'form':form
  }
  return render(request,'myapp/index.html',params)