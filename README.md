`sudo adduser son`<br>
`sudo usermod -aG sudo son`<br>
<br>
`sudo apt update && sudo apt upgrade -y`<br>
`sudo apt install python3 python3-pip python3-venv -y`<br>
<br>
`mkdir myproject`<br>
`cd myproject`<br>
<br>
`python3 -m venv django_env`<br>
`source django_env/bin/activate`<br>
<br>
`pip3 install django`<br>
`django-admin startproject myproject`<br>
`cd myproject`<br>
`python3 manage.py startapp blog`<br>
`nano myproject/settings.py`<br>
`INSTALLED_APPS = ['blog']`<br>
`ALLOWED_HOSTS = ['*']`<br>
`nano myapp/models.py`<br>
`from django.db import models`<br>
```
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

```
`nano myapp/admin.py`<br>
```
from django.contrib import admin
from .models import Category, Tag, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
```
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
`python3 manage.py runserver 0.0.0.0:8000`
