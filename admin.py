from django.contrib import admin
from .models import Campaign, Article

class CampaignAdmin(admin.ModelAdmin):
    list_display = ("campaign_name", "campaign_create_time", "campaign_status", "campaign_type")
    search_fields = ("campaign_name", "campaign_status")
    readonly_fields = [
        'campaign_create_time', 'campaign_auto_params_cpm', 'campaign_auto_params_subject_name', 
        'campaign_auto_params_subject_id', 'campaign_name', 'campaign_auto_params_nms', 
        'campaign_advert_id', 'campaign_status', 'campaign_type'
    ]
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'article_wb', 'article_1c', 'article_sku', 'article_residue'
    ]
admin.site.register(Campaign, CampaignAdmin) 
admin.site.register(Article, ArticleAdmin)