import requests
from wb.models import Campaign, Article

api_url = "https://advert-api.wildberries.ru/adv/v1/promotion/adverts?type=8&order=change&direction=asc"
api_key = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwNzE1djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTczODA5MzY3MCwiaWQiOiJhNjA3ODg5NS1iNjFlLTQ5ZDEtYmQwZS1mM2FjNTJiNDU2OWYiLCJpaWQiOjE1MTE1NjYxMCwib2lkIjoxMDU4ODEwLCJzIjo4MTkwLCJzaWQiOiJkYjM1NjRiYy04MGYwLTQ5OGYtOGVkZC00NjkxZTQ0NTYwMTAiLCJ0IjpmYWxzZSwidWlkIjoxNTExNTY2MTB9.h4A6DP8kxL6UJo3WR92TvjIQjQW-Pm1wj4JaA8Nxb6PvhzhrMMx22bBGVDFOzQQRXeTqdDO4lyzduq-vPxiUsw"
headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}
response = requests.post(api_url, headers=headers, json=[])
data = response.json()

for item in data:
    campaign_create_time = item.get('createTime')
    campaign_auto_params = item.get('autoParams', {})
    campaign_auto_params_cpm = campaign_auto_params.get('cpm')
    campaign_auto_params_subject = campaign_auto_params.get('subject', {})
    campaign_auto_params_subject_name = campaign_auto_params_subject.get('name')
    campaign_auto_params_subject_id = campaign_auto_params_subject.get('id')

    campaign_auto_params_nms = campaign_auto_params.get('nms') or []

    campaign_name = item.get('name')
    campaign_advert_id = item.get('advertId')
    campaign_status = item.get('status')
    campaign_type = item.get('type')

    campaign_instance, created = Campaign.objects.update_or_create(
        campaign_advert_id=campaign_advert_id,
        defaults={
            'campaign_create_time': campaign_create_time,
            'campaign_auto_params_cpm': campaign_auto_params_cpm,
            'campaign_auto_params_subject_name': campaign_auto_params_subject_name,
            'campaign_auto_params_subject_id': campaign_auto_params_subject_id,
            'campaign_name': campaign_name,
            'campaign_status': campaign_status,
            'campaign_type': campaign_type,
        }
    )

    campaign_instance.campaign_auto_params_nms.clear()

    for nms_code in campaign_auto_params_nms:
        article_instance, _ = Article.objects.get_or_create(article_wb=nms_code)
        campaign_instance.campaign_auto_params_nms.add(article_instance)