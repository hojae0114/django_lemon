from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title

def user_path(instance, filename):
        from random import choice
        import string
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr) # 8자리 임의 파일명
        extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
        return '%s/%s.%s' % (instance.owner.username, pid, extension) #ex abcdefgs.png

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path) # 어디로 업로드 할지
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 로그인 한 사용자
    thumname_image = models.ImageField(blank = True) #입력안해도 됨
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성



























