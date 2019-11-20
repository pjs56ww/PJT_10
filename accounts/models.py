from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# User 모델 Customizing
# pass : default, 확장성을 위해 쓰지 말고 커스터마이징 할 것.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        # related_name : 꼭 필요한 건 아니지만 역참조를 위해 필요함.
        related_name='following'
    )

# settings.py 에 AUTH_USER_MODEL = 'accounts.User' 반드시 등록