import time, datetime

from django.contrib import admin
from articles.models import Article
from django.utils.timezone import make_aware
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('date', 'content', 'admin_create_at', 'admin_update_at')
    display = ('create_at', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    
    @admin.display(description='Create Time')
    def admin_create_at(self, obj):
        return make_aware(datetime.datetime.fromtimestamp(obj.create_at))
    
    @admin.display(description='Update Time')
    def admin_update_at(self, obj):
        return make_aware(datetime.datetime.fromtimestamp(obj.update_at))
    
admin.site.register(Article, ArticleAdmin)


@receiver(pre_save, sender=Article)
def update_at(sender, instance, **kwargs):
    instance.update_at = int(time.time())