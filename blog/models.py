from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类与标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    #自定义 get_absolute_url方法
    #记得从diango.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


