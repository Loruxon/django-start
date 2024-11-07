from django.db import models

class Article(models.Model):
    article_wb = models.CharField(max_length=255, unique=True, verbose_name="Артикул WB")
    article_1c = models.CharField(max_length=255, null=True, blank=True, verbose_name="Артикул 1С")
    article_sku = models.CharField(max_length=255, null=True, blank=True, verbose_name="SKU")
    article_payout = models.CharField(max_length=255, null=True, blank=True, verbose_name="Маржа")
    article_residue = models.CharField(max_length=255, null=True, blank=True, verbose_name="Остаток")
    article_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название")

    def __str__(self):
        return self.article_wb

class Campaign(models.Model):
    campaign_create_time = models.DateTimeField(null=True, blank=True, verbose_name="Время создания кампании")
    campaign_auto_params_cpm = models.CharField(max_length=255, null=True, blank=True, verbose_name="Средний CPM")
    campaign_auto_params_subject_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Категория")
    campaign_auto_params_subject_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="ID категории")
    campaign_auto_params_nms = models.ManyToManyField(Article, related_name='campaigns', blank=True, verbose_name="Артикулы WB")
    campaign_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название кампании")
    campaign_advert_id = models.CharField(max_length=255, unique=True, verbose_name="ID кампании")
    campaign_status = models.CharField(max_length=255, null=True, blank=True, verbose_name="Статус")
    campaign_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип кампании")

    def __str__(self):
        return self.campaign_name