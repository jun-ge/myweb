from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    # null 默认不允许为null     null = True 表示不能为null
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=31)
    sex = models.CharField(max_length=1, default='1')
    create_date = models.DateTimeField(auto_now_add=True)

    # 唯一  自动创建索引
    class Meta:
        # abstract = True
        db_table = 'T_USER'
        # 默认是升序   -表示降序 ? 随机排序
        ordering = ['create_date', ]
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        # indexes = ['phone', ]
    def __str__(self):
        return self.username

# phone = models.DateTimeField(auto_now_add=True)
# create_date = models.DateTimeField(default=timezone.now())


class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title