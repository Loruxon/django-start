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
`python3 manage.py startapp wb`<br>
`nano myproject/settings.py`<br>
`INSTALLED_APPS = ['wb']`<br>
`ALLOWED_HOSTS = ['*']`<br>
`nano wb/models.py`<br>
```
from django.db import models

class Adv(models.Model):
    adv_create_time = models.DateTimeField(null=True, blank=True)  # Время создания
    adv_auto_params_cpm = models.FloatField(null=True, blank=True)  # CPM
    adv_auto_params_subject_name = models.CharField(max_length=255, null=True, blank=True)  # Название темы
    adv_auto_params_subject_id = models.IntegerField(null=True, blank=True)  # Идентификатор темы
    adv_auto_params_nms = models.TextField(null=True, blank=True)  # Список NMS
    adv_name = models.CharField(max_length=255, null=True, blank=True)  # Название рекламы
    adv_advert_id = models.IntegerField(unique=True)  # Идентификатор рекламы (уникальный)
    adv_status = models.CharField(max_length=50, null=True, blank=True)  # Статус рекламы
    adv_type = models.CharField(max_length=50, null=True, blank=True)  # Тип рекламы

    def __str__(self):
        return self.adv_name
```
`nano wb/update_adv.py`<br>
```
import requests
from wb.models import Adv

api_url = "https://advert-api.wildberries.ru/adv/v1/promotion/adverts?type=8&order=change&direction=asc"
api_key = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwNzE1djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTczODA5MzY3MCwiaWQiOiJhNjA3ODg5NS1iNjFlLTQ5ZDEtYmQwZS1mM2FjNTJiNDU2OWYiLCJJpaWQiOjE1MTE1NjYxMCwib2lkIjoxMDU4ODEwLCJzIjo4MTkwLCJzaWQiOiJkYjM1NjRiYy04MGYwLTQ5OGYtOGVkZC00NjkxZTQ0NTYwMTAiLCJ0IjpmYWxzZSwidWlkIjoxNTExNTY2MTB9.h4A6DP8kxL6UJo3WR92TvjIQjQW-Pm1wj4JaA8Nxb6PvhzhrMMx22bBGVDFOzQQRXeTqdDO4lyzduq-vPxiUsw"
headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}
response = requests.post(api_url, headers=headers, json=[])
data = response.json()
for item in data:
    adv_create_time = item.get('createTime')
    adv_auto_params = item.get('autoParams', {})
    adv_auto_params_cpm = adv_auto_params.get('cpm')
    adv_auto_params_subject = adv_auto_params.get('subject', {})
    adv_auto_params_subject_name = adv_auto_params_subject.get('name')
    adv_auto_params_subject_id = adv_auto_params_subject.get('id')
    adv_auto_params_nms = ", ".join(map(str, adv_auto_params.get('nms', [])))
    adv_name = item.get('name')
    adv_advert_id = item.get('advertId')
    adv_status = item.get('status')
    adv_type = item.get('type')

    Adv.objects.update_or_create(
        adv_advert_id=adv_advert_id, defaults={
            'adv_create_time': adv_create_time,
            'adv_auto_params_cpm': adv_auto_params_cpm,
            'adv_auto_params_subject_name': adv_auto_params_subject_name,
            'adv_auto_params_subject_id': adv_auto_params_subject_id,
            'adv_auto_params_nms': adv_auto_params_nms,
            'adv_name': adv_name,
            'adv_status': adv_status,
            'adv_type': adv_type,
        }
    )
```
`python manage.py shell`<br>
`from myapp.import_ads import *`<br>
`nano wb/admin.py`<br>
```
from django.contrib import admin
from .models import Adv

admin.site.register(Adv)
```
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
`python3 manage.py runserver 0.0.0.0:8000`
