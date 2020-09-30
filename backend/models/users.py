from django.db import models
from django.contrib.auth.models import AbstractUser

from librarys.utils.strings import get_uuid


class Users(AbstractUser):
    id = models.CharField(max_length=64, primary_key=True, default=get_uuid())
    create_date = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    nickname = models.CharField(max_length=32, blank=True, null=True, verbose_name='昵称')
    sex = models.CharField(max_length=8, default='男')
    is_superuser = models.BooleanField()
    remark = models.CharField(max_length=32, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return f"<{self.username}> Model"
