from django.db import models

# Create your models here.
GAME_LANK = (('1','ルーキー'),('2','ブロンズ'),('3','シルバー'),('4','ゴールド'),('5','プラチナ'),('6','ダイアモンド'),('7','マスター'),('8','プレデター'))
HOW_TO_PLAY = (('1','ランクマッチがやりたい'),('2','カジュアルマッチがやりたい'),('3','ランクを上げたい'),('4','カジュアルに遊びたい'),('5','フレンドになりたい'),('6','今回限り'),('7','長く遊べるフレンド募集'))
SEX = (('1','男性'),('2','女性'),('3','秘密'))

class User(models.Model):
  username = models.TextField(max_length=20)
  password = models.TextField(max_length=20)
  mail = models.EmailField()

class UserDetails(models.Model):
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)
  sex = models.CharField(max_length=5,choices=SEX,null=True,blank=True)
  img_name = models.ImageField(null=True,blank=True)
  game_lank = models.CharField(max_length=10,choices=GAME_LANK,null=True,blank=True) # GAME_LANKから選択
  like_weapons = models.CharField(max_length=50,null=True,blank=True)
  how_to_play = models.CharField(max_length=20,choices=HOW_TO_PLAY,null=True,blank=True)
  play_timezone = models.CharField(max_length=50,null=True,blank=True)
  self_intro = models.TextField(null=True,blank=True)
  ps_id = models.CharField(max_length=30,null=True,blank=True)

class Platform(models.Model):
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)
  play_station = models.BooleanField(default=False)
  x_box = models.BooleanField(default=False)
  switch = models.BooleanField(default=False)
  pc  = models.BooleanField(default=False)
