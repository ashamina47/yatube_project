from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Группy'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default='Пусто')
    slug = models.SlugField(unique=True, null=True, default='post')
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=122)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    group = models.ForeignKey(Group,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='posts')

    def __str__(self):
        return self.title
