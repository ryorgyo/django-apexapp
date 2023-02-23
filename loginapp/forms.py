from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      self.label_suffix = ''
      
      for field in self.fields.values():
        field.widget.attrs['placeholder'] = field.label
        field.widget.attrs.update({'class':'w-80 h-12 border border-gray-600 border-solid mb-10'})

# class NewAccountForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.label_suffix = " "
#         for field in self.fields.values():
#           field.widget.attrs['placeholder'] = field.label
#           field.widget.attrs.update({'class':'w-80 h-12 border border-gray-600 border-solid mb-10'})

#     sex_choices = (('1','男性'),('2','女性'),('3','秘密'))
#     game_lank_choices = (('1','ルーキー'),('2','ブロンズ'),('3','シルバー'),('4','ゴールド'),('5','プラチナ'),('6','ダイアモンド'),('7','マスター'),('8','プレデター'))
#     how_to_play_choices = (('1','ランクマッチがやりたい'),('2','カジュアルマッチがやりたい'),('3','ランクを上げたい'),('4','カジュアルに遊びたい'),('5','フレンドになりたい'),('6','今回限り'),('7','長く遊べるフレンド募集'))

#     sex = forms.fields.ChoiceField(choices=sex_choices,label='性別')
#     game_lank = forms.fields.ChoiceField(choices=game_lank_choices,label='ランク帯')
#     how_to_play = forms.fields.ChoiceField(choices=how_to_play_choices,label='求めるフレンド')

#     class Meta:
#         model = User
#         fields = '__all__'
#         labels = {'username':'ユーザー名','password':'パスワード','img_name':'プロフィール画像','like_weapons':'好きな武器','play_timezone':'よくやる時間帯','self_intro':'自己紹介','ps_id':'PlayStationID'}

class NewAccountForm(forms.ModelForm):
    confirm = forms.CharField(max_length=20,label='パスワード（確認用）')
    field_order =['username','password','confirm','mail']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
        for field in self.fields.values():
          field.widget.attrs['placeholder'] = field.label
          field.widget.attrs.update({'class':'w-80 h-12 border border-gray-600 border-solid mb-10'})
    class Meta:
        model = User
        fields = '__all__'
        labels = {'username':'ユーザー名','mail':'メールアドレス','password':'パスワード'}