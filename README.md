```python
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y

pip3 install django
django-admin startproject myproject
cd myproject
python3 manage.py startapp blog

nano myproject/settings.py
INSTALLED_APPS = [
    'blog',
]
ALLOWED_HOSTS = ['*']

nano myapp/models.py
from django.db import models

class Category(models.Model):
    category_url = models.SlugField(unique=True, verbose_name="URL категории")
    category_name = models.CharField(max_length=200, verbose_name="Название категории")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    tag_url = models.SlugField(unique=True, verbose_name="URL тега")
    tag_name = models.CharField(max_length=200, verbose_name="Название тега")

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    post_url = models.SlugField(unique=True, verbose_name="URL поста")
    post_keywords = models.CharField(max_length=255, verbose_name="Ключевые слова")
    post_description = models.TextField(verbose_name="Описание")
    post_title = models.CharField(max_length=200, verbose_name="Заголовок")
    post_text = models.TextField(verbose_name="Текст")

    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


nano myapp/admin.py
from django.contrib import admin
from .models import Category, Tag, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
